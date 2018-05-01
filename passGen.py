import random

wordFile = open("static/eff-short.txt", 'r')
wordList = wordFile.readlines()

specialwordfilenames=["static/adj.txt", "static/noun.txt", "static/verb.txt", "static/adverbs.txt"]
speicalwordslists=[open(wordFile,"r").readlines() for wordFile in specialwordfilenames]


def altscore(word):
   score = 0.0
   leftHand = "asdfgzxcvbqwert"
   rightHand = "lkjhpoiuymn"
   for i in range(len(word)-1):
       if word[i] in leftHand and word[i+1] in rightHand:
           score += 1
       elif word[i] in rightHand and word[i+1] in leftHand:
           score += 1
       elif word[i] == word[i+1]:
           score += 1

   return score / (len(word)-1)


def makePassword(goodwords,maxLen):
    done = False
    while not done:
        passlist = []
        for i in range(4):
            passlist.append(goodwords[random.randrange(len(goodwords))])
        wlen = len("".join(passlist))
        if wlen <= maxLen and wlen > 10:
            done = True
            passlist.append(wlen)
    return passlist


def wordFilter(word,minl,maxl,alt):
    w = word[:-1]
    if len(w) >= minl and len(w) <= maxl:
        if alt:
            return altscore(w) >= 0.7
        else:
            return True
    return False


def makePasswordList(minLen,maxLen,maxPw,alt):
    goodwords = [word[:-1] for word in wordList
                     if wordFilter(word,minLen,maxLen,alt)]

    wlist = []
    for i in range(10):
        wlist.append(makePassword(goodwords,maxPw))
    return wlist


def doLetterSubs(pwlist):
    for row in pwlist:
        i = 0
        done = False
        while i < len(row)-1 and not done:
            newword = row[i].replace('e','3')
            newword = newword.replace('o','0')
            if newword != row[i]:
                row[i] = newword
                done = True
            i += 1


def makeSpecialPassword(goodwordslists,maxLen):
    done = False
    while not done:
        passlist = []
        mina=min(len(list) for list in goodwordslists)
        for i in range(4):
            passlist.append(goodwordslists[i][random.randrange(mina)])
        wlen = len("".join(passlist))
        if wlen <= maxLen and wlen > 10:
            done = True
            passlist.append(wlen)
    return passlist


def specialPasswordList(minLen,maxLen,maxPw,alt):
    goodwordslists=[[word[:-1] for word in wordList if wordFilter(word,minLen,maxLen,alt)] for wordList in speicalwordslists]

    wlist = []
    for i in range(10):
        wlist.append(makeSpecialPassword(goodwordslists,maxPw))
    return wlist


if __name__ == '__main__':
    print(makePasswordList(4,7,25,True))
    print(specialPasswordList(5,10,100,False))