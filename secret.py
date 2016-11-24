from Crypto.Cipher import DES
import base64

def pad(s): return s+(8-len(s)%8)*chr(8-len(s)%8)

msg="The cake is a lie!\n"
key="1337DEADBEEF1664".decode('hex')
iv="0102030405060708".decode('hex')
cipher=DES.new(key,DES.MODE_CBC,iv)
print base64.encodestring(cipher.encrypt(pad(msg)))
