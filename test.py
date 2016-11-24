import ed25519

sk=32*chr(0)
pk=ed25519.publickey(sk)
print "publickey for 0 is", pk.encode('hex')

for i in [0,1,10]:
  print "encodeint %d = %s" % (i,ed25519.encodeint(i).encode('hex'))

for p in [(0,0),(1,1),(10,0),(1,10),(9639205628789703341510410801487549615560488670885798085067615194958049462616,18930617471878267742194159801949745215346600387277955685031939302387136031291)]:
  print "encodepoint %s = %s" % (repr(p),ed25519.encodepoint(p).encode('hex'))

msg="This is a secret message"
sig=ed25519.signature(msg,sk,pk)
print 'signature("%s") = %s' % (msg, sig.encode('hex'))
try:
  ed25519.checkvalid(sig,msg,pk)
  print 'check signature result: true'
except:
  print 'check signature result: false'
