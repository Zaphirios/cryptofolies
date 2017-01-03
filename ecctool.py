#!/bin/env python
import sys
import argparse
import ed25519
import generateurKeystore
from os import urandom
from base64 import b64encode


parser = argparse.ArgumentParser(description='Elliptic curve cryptography toolkit.')

parser.add_argument('-keygen', action='store', dest='keygen', help='Generate key pair')
parser.add_argument('-exportpub', action='store_true', dest='export_pub', help='Export public key', default=False)
parser.add_argument('-importpub', action='store_true', dest='import_pub', help='Import public key', default=False)
parser.add_argument('-sign', action='store_true', dest='sign', help='Sign a message', default=False)
parser.add_argument('-check', action='store_true', dest='check', help='Check the integrity of a signed message', default=False)
parser.add_argument('-sig', action='store', dest='sig', help='File to check')
parser.add_argument('-enc', action='store', dest='enc', help='Encrypt a file')
parser.add_argument('-dec', action='store', dest='dec', help='Decrypt a file')

parser.add_argument('-id', action='store', dest='user_id', help='Set identity')
parser.add_argument('-in', action='store', dest='in_info', help='Input file')
parser.add_argument('-out', action='store', dest='out_info', help='Output file')
parser.add_argument('-dest', action='store', dest='dest', help='Id of the recipient')



args = parser.parse_args()

# ecctool -keygen DSA-Ed25519-SHA-512 -id alice
if args.keygen :
    if args.user_id :
        print("Generation de la clef pour : "+args.user_id)
        retour =  generateurKeystore.generationKey(args.user_id)
        if retour == -1:
            print("une erreur s'est deroulee durant l'execution")
        else :
            print("clef generes")

    else :
        print("[ERREUR] -id manquant")

# ecctool -exportpub -id alice
elif args.export_pub :
    if args.user_id :
        print("exportation de la clef pub")
        info = generateurKeystore.exportPub(args.user_id)
        print("voici les info sur votre clef : \n")
        print("    - chiffrement : " + info[1] + "\n")
        print("    - voici votre clef publique : " + info[2] + "\n")
        # TODO methode exportPub() dans generateur keystore

    else :
        print("[ERREUR] -id manquant")

# ecctool -importpub -id bob < bobkey.txt
elif args.import_pub :
    if args.user_id :
        print("arg4 :4" + sys.argv[4])
        generateurKeystore.importPub(args.user_id, sys.argv[4])
        print("importation depuis un fichier")

    else :
        print("[ERREUR] -id manquant")

# ecctool -sign -id alice -in message.txt -out message.sig
elif args.sign :
    action = 0

    if action != -1 and args.user_id :
        action = 1
    else :
        action = -1
        print("[ERREUR] -id manquant")

    if action != -1 and args.in_info :
        action = 2
    else :
        action = -1
        print("[ERREUR] -in manquant")

    if action != -1 and args.out_info :
        action = 3
    else :
        action = -1
        print("[ERREUR] -out manquant")

    if action == 3 :
        print("signature du message")
        fichier = open("message.txt", "r")
        msg = fichier.read()
        fichier.close()

        info_pk = generateurKeystore.exportPub(args.user_id)
        info_sk = generateurKeystore.exportSec(args.user_id)
        if info_pk < 0 or info_pk < 0:
            print "erreur id introuvable"
        else:

            userPK = info_pk[2]
            userSK = info_sk[2]

            userPK = str(userPK).rstrip().decode('hex')
            userSK = str(userSK).rstrip().decode('hex')


            sig = ed25519.signature(msg, userSK, userPK)
            fichier = open(args.out_info, "w")
            fichier.write(sig.encode("hex"))
            fichier.close()

            print "la signature a ete generee"


#ecctool -check -in message.txt -sig message.sig -id alice
elif args.check :
    action = 0

    if action != -1 and args.in_info :
        action = 1
    else:
        print("[ERREUR] -in manquant")


    if action != -1 and args.sig :
        action = 2
    else:
        print("[ERREUR] -sig manquant")

    if action != -1 and args.user_id :
        action = 3
    else:
        print("[ERREUR] -id manquant")

    if action == 3 :
        print("check signature du message")
        fichier = open(args.in_info, "r")
        msg = fichier.read()
        fichier.close()
        info_pk = generateurKeystore.exportPub(args.user_id)
        info_sk = generateurKeystore.exportSec(args.user_id)
        if info_sk < 0:
            print "erreur id introuvable"
        else:
            userPK = info_pk[2]
            userSK = info_sk[2]

            userPK = str(userPK).rstrip().decode('hex')
            userSK = str(userSK).rstrip().decode('hex')

            fsig = open(args.sig, "r")
            signature = fsig.read()
            fsig.close()

            signature = str(signature).rstrip().decode('hex')

            try:
                ed25519.checkvalid(signature, msg, userPK)
                print "La signature est conforme"
            except:
                print "la signature est fausse"

# ecctool -enc -dest bob -in message.txt -out message.crypt
elif args.enc :
    action = 0

    if action != -1 and args.dest :
        action = 1
    else:
        print("[ERREUR] -dest manquant")

    if action != -1 and args.in_info:
        action = 2
    else:
        print("[ERREUR] -in manquant")

    if action != -1 and args.out_info:
        action = 3
    else:
        print("[ERREUR] -out manquant")

    if action == 3:
        print("encryptage du fichier")

    abort = False
    #on verifie que le destinataire a une clef
    info_pk = generateurKeystore.exportPub(args.user_id)
    if info_pk < 0:
        abort = True
        print "Destinaire n'a pas de clef"



    fichier = open(args.sig, "r")
    message = fichier.read()
    fichier.close()
    if abort is False and message == "":
        abort = True
        print "Le message est vide"




# ecctool -dec -id alice -in secret.crypt -out secret.txt
elif args.dec:
    action = 0

    if action != -1 and args.dest:
        action = 1
    else:
        print("[ERREUR] -dest manquant")

    if action != -1 and args.in_info:
        action = 2
    else:
        print("[ERREUR] -in manquant")

    if action != -1 and args.out_info:
        action = 3
    else:
        print("[ERREUR] -out manquant")

    if action == 3:
        print("decryptage du fichier")
    #TODO decryptage du ficher

else :
    print("commande imcomprise")
