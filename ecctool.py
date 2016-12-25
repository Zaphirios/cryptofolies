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
parser.add_argument('-in', action='store', dest='in', help='Input file')
parser.add_argument('-out', action='store', dest='out', help='Output file')
parser.add_argument('-dest', action='store', dest='dest', help='Id of the recipient')



args = parser.parse_args()
if args.keygen :
    if args.user_id :
        print(args.user_id)
        print("debut de la generation de la clef")
        generateurKeystore.generationKey(args.user_id)
        print("clef generes")

    else:
        print("veuillez rajouter l'id de la personne")


print(args.keygen)
