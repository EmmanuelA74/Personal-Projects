from itertools import permutations
import re
# 1
print('Hello!, Welcome to the Scrabble Word Finder!')
print('Enter the words in your tray.')
words = input()

filename = 'scrabble_dict.txt'
dictionary = []
with open(filename) as file :
    contents = file.read().split()
    for word in contents :
        dictionary.append(word.strip())

tilescores = {'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':8,'k':5,'l':1,'m':3,'n':1,'o':1,'p':3,'q':10,'r':1,'s':1,'t':1,'u':1,'v':4,'w':4,'x':8,'y':4,'z':10}      
#2
new = list(words)
for x in new :
    if x == ' ' :
        new.remove(x)
load = ''.join(new)
Load = load.lower()

# 3 and #4
Find = []
v = 2
while v < (len(load) + 1) :
    print('working on words of length', v)
    perm = list(permutations(Load, v))
    for x in range(len(perm)) :
        perm[x] = ''.join(perm[x])
        if perm[x] in dictionary and perm[x] not in Find :
            Find.append(perm[x])
    v += 1

def scrabble_score(word):
    total = 0
    for i in word:
        total = total + tilescores[i]
    return total

Find.sort(reverse = True, key = scrabble_score)
for x in Find :
    print(x, ':', scrabble_score(x))


