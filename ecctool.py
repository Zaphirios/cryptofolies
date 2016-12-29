#!/bin/env python

import argparse
import generateurKeystore

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
		print(args.user_id)
		print("debut de la generation de la clef")
		generateurKeystore.generationKey(args.user_id)
		print("clef generes")
	else:
		print("[ERREUR] -id manquant")

# ecctool -exportpub -id alice
elif args.export_pub :
	if args.user_id :
		print("exportation de la clef pub")
		# TODO methode exportPub() dans generateur keystore

	else :
		print("[ERREUR] -id manquant")

# ecctool -importpub -id bob < bobkey.txt
elif args.import_pub :
	if args.user_id :
		print("importation depuis un fichier")
		#TODO import depuis un fichier existant

	else :
		print("[ERREUR] -id manquant")

# ecctool -sign -id alice -in message.txt -out message.sig
elif args.sign :
	action = 0

	if action != -1 and user_id :
		action = 1
	else :
		action = -1
		print("[ERREUR] -id manquant")

	if action != -1 and args.in_info :
		action = 2
	else :
		action = -1
		print("[ERREUR] -in manquant")

	if action != -1 and args.out :
		action = 3
	else :
		action = -1
		print("[ERREUR] -out manquant")

	if action == 3 :
		print("signature du message")
		# TODO methode pour signer des message

#ecctool -check -in message.txt -sig message.sig
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

	if action == 2 :
		print("check signature du message")
		#TODO check signature message

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
		#TODO encryptage du ficher

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


print(args.keygen)
