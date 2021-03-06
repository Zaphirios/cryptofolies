from Crypto.Cipher import AES
import base64

def pad(s): return s+(16-len(s)%16)*chr(1)
def unpad(s): return s.translate(None, chr(1))


def encrypt(key, message, iv):
    key=pad(key)[:32].encode()
    iv=pad(iv)[:16].encode()
    cipher=AES.new(key,AES.MODE_CBC,iv)
    return base64.encodestring(cipher.encrypt(pad(message.decode())))

def decrypt(key, message, iv):

    key=pad(key)[:32].encode()
    iv=pad(iv)[:16].encode()
    cipher=AES.new(key,AES.MODE_CBC,iv)
    return unpad(cipher.decrypt(base64.decodestring(message)))
