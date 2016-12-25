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
