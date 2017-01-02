from os import urandom
import ed25519
from os.path import exists

def init_fichier():
    fichier = open("keystore","w")
    fichier.write("[PUB]\n")
    fichier.write("\n")
    fichier.write("[/PUB]\n")
    fichier.write("[SEC]\n")
    fichier.write("\n")
    fichier.write("[/SEC]\n")
    fichier.close()
    return


def generationKey(nomUser):
    if exists("keystore") == False :
        print("creation du keystore")
        init_fichier()


    user = urandom(256/8).encode('hex')

    fichier = open("keystore", "r")
    pub = 0
    sec = 0
    toWrite = ""
    for ligne in fichier:
        nom = ligne.split(":")
        if nom[0] == nomUser:
            print("[ERREUR] Le nom existe deja ! ")
            return -1 #oui cest degue mais si quelque veux faire le projet qu'il le fasse

        if ligne == "[PUB]\n":
            pub = 1
            sec = 0

        if ligne == "[SEC]\n":
            pub = 0
            sec = 1


        if ligne == "[/PUB]\n" and pub == 1:
            toWrite = toWrite + nomUser+":DSA-Ed25519-SHA-512:"+ed25519.publickey(user).encode('hex')+"\n"
            pub = 0
            toWrite = toWrite + ligne
        elif ligne == "[/SEC]\n" and sec == 1:
            toWrite = toWrite + nomUser+":DSA-Ed25519-SHA-512:"+user+"\n"
            sec = 0
            toWrite = toWrite + ligne
        else:
            toWrite = toWrite + ligne
    fichier.close()
    fichier = open("keystore", "w")
    fichier.write(toWrite)
    fichier.close()
    return

def exportPub(user_id):
    if exists("keystore") == False:
        print("Fichier keystore inexistant")
        return -1

    fichier = open("keystore", "r")
    chercher = False
    for ligne in fichier:
        if chercher == False and ligne == "[PUB]\n":
            chercher = True;

        elif chercher == True and ligne == "[/PUB]\n":
            chercher = False

        elif chercher == True:
            info = ligne.split(':')
            if info[0] == user_id:
                return info

    return

def importPub(user_id, key):
    if exists("keystore") == False:
        print("creation du keystore")
        init_fichier()


    print(key)
    return
