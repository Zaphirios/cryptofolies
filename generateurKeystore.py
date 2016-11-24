from os import urandom
import ed25519

alice = urandom(256/8).encode('hex')
bob = urandom(256/8).encode('hex')


fichier = open("keystore", "a")

fichier.write("[pub]\n")
fichier.write("alice:DSA-Ed25519-SHA-512:"+ed25519.publickey(alice).encode('hex')+"\n")
fichier.write("bob:DSA-Ed25519-SHA-512:"+ed25519.publickey(bob).encode('hex')+"\n")

fichier.write("[sec]\n")
fichier.write("alice:DSA-Ed25519-SHA-512:"+alice+"\n")
fichier.write("bob:DSA-Ed25519-SHA-512:"+bob+"\n")