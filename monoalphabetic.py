# Alternate, simplified monoalphabetic cipher methods
# which preserve case and do not alter punctuation

import sys
import string

def formatKey(text):
    text = filter(lambda c: c.isalpha(), text)  #only grab alphabetic characters
    text = text.lower()   #change to lowercase
    
    seen = set()
    for c in text:    #check that all 26 letters were used in key exactly once
        if c not in seen:
            seen.add(c)
            
    if len(seen) == 26:    #letters used exactly once
        return text
    else:
        print "Error: Key does not use each letter exactly once"
        sys.exit(1)
        
        
def encrypt(key, plaintext):
    
    formatKey(key)
    
    inTable = string.ascii_lowercase + string.ascii_uppercase
    outTable = key.lower() + key.upper()
    transTable = string.maketrans(inTable, outTable)
    
    return plaintext.translate(transTable)
    
def decrypt(key, ciphertext):

    formatKey(key)
    
    inTable = key.lower() + key.upper()
    outTable = string.ascii_lowercase + string.ascii_uppercase
    transTable = string.maketrans(inTable, outTable)
    
    return ciphertext.translate(transTable)

'''    
fookey = "qwertyuiopasdfghjklzxcvbnm"
foopt = "pYtHon is $$@)(!* FUn"
foobar = encrypt(fookey, foopt)
fizzbuzz = decrypt(fookey, foobar)

print "original: %s" % (foopt)
print "encrypted: %s" % (foobar)
print "decrypted: %s" % (fizzbuzz)
'''