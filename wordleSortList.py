import re

lines = []
wordList = []

with open('list2.txt', encoding="utf-8" ) as f:
    lines = f.readlines()
    for line in lines:
        l = line.lstrip()
        words = l.split(' ')
        if(len(words) == 1 and re.match(r"^[a-z]{5}$", l)):
            w = l.strip('\n').lower()
            if not w in wordList:
                wordList.append(l.strip('\n').lower())

alphabet = 'abcdefghijklmnopqrstuvwxyz'
tally = [0] * len(alphabet)
orderTally = [[0] * len(alphabet), [0] * len(alphabet), [0] * len(alphabet), [0] * len(alphabet), [0] * len(alphabet)]

for word in wordList:
    j = 0
    for c in word:
        i = ord(c) - ord('a')
        tally[i] = tally[i] + 1
        orderTally[j][i] += 1
        j+=1

def sumWord(w):
    sum = 0
    used = []
    for c in w:
        if not c in used:
            i = ord(c) - ord('a')
            sum += tally[i]
            used.append(c)
    return sum

def letterOrder(w):
    sum = 0
    j = 0
    for c in w:
        i = ord(c) - ord('a')
        sum += orderTally[j][i]
        j+=1
    return sum

wordList = list(sorted(wordList, key=lambda x: (sumWord(x), letterOrder(x)), reverse=True))

with open('list2.txt', 'w') as f:
    for word in wordList:
        f.write(f'"{word}"\n')