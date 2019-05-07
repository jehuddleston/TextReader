import sys
from random import choice

def capFirstLetter(word):
    if len(word) < 2:
        return word.upper()
    else:
        return word[0].upper() + word[1:]

def generate():
    if len(sys.argv) is not 4 and len(sys.argv) is not 5:
        return "ERROR: generate has the form generate <source> <dest>"
    else:
        src = sys.argv[2]
        dest = sys.argv[3]
        f = open(src,'r')
        mapdict = dict(eval(f.read()))
        f.close()

        text = ""

        numSentences = 0
        if len(sys.argv) is 5:
            numSentences = int(sys.argv[4])
        else:
            for key in mapdict:
                if "$" in mapdict[key]:
                    numSentences = numSentences + 1
        currWord = "$"
        numGenerated = 0
        while(numGenerated <= numSentences):
            nextWord = choice(mapdict[currWord])
            if nextWord == "$":
                currWord = "$"
                numGenerated = numGenerated + 1
                text = text + "."
                if(numGenerated <= numSentences):
                    while(nextWord is "$"):
                        nextWord = choice(mapdict[currWord])

                        nextWord = capFirstLetter(nextWord)
                else:
                    nextWord = ""
            elif currWord == "$":
                nextWord = capFirstLetter(nextWord)
            text = text + " " + nextWord
            currWord = nextWord.lower()


        f = open(dest,'w')
        f.write(text)
        f.close()

        return "generated text to " + dest
