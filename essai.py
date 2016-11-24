# -*- coding: utf-8 -*-
from sha512 import sha512

print "SHA512 de la chaîne 'Coucou':"
print sha512('Coucou').hexdigest()

from os import urandom
print "256 bits de qualité crypto",urandom(256/8).encode('hex')
