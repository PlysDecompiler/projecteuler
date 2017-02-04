#https://projecteuler.net/problem=42

s = open('words.txt', 'r').read()

wordlist = eval(s)
numtriwords = 0
# here I made a test that found out the maxlength of a word
# print max([len(w) for w in wordlist])
# which equaled to 14 so the maximum trianglenumber ist 26*14 = 364
trinums = []
n = 1
while (0.5*n*(n+1)) <= 364:
    trinums.append((0.5*n*(n+1)))
    n+=1

for word in wordlist:
    if sum(ord(c)-64 for c in word) in trinums:
        numtriwords += 1

print numtriwords         
#solution: 162
