#https://projecteuler.net/problem=59

cipher = [int(char) for char in open('cipher.txt', 'r').read().split(',')]
common = ['the', 'in', 'as', 'key', 'text', 'message']

#print len(cipher)
#found that cipher has 1201 characters

filtered = []
def decrypt(ciph, key):
    s = ''
    for i, c in enumerate(ciph):
        s += chr(c ^ key[i%3])
    return s

#a: 97... z: 122
for a in range(97,123):
    for b in range(97,123):
        for c in range(97,123):
            candidate = decrypt(cipher, [a,b,c])
            wordlist = candidate.lower().split(' ')
            if len(wordlist)>100:
                if any(c in wordlist for c in common):
                    print ' '.join(wordlist)
                    print a,b,c

#after seeing the 6 candidates that survived this filter I conclude that a=103='g', b=111='o', c=100='d'
text = decrypt(cipher, [103,111,100])
print sum([ord(i) for i in text])

#solution: 107359
