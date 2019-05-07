import sys
import re

def load():
    if((len(sys.argv) is not 4) and (len(sys.argv) is not 5)):
        return "ERROR: load has the form load <source> <dest> <reuse dict(optional)>"
    filename = sys.argv[2]
    dest = sys.argv[3]
    keep = False
    if(len(sys.argv) is 5):
        if(sys.argv[4] == "-k"):
            keep = True
        else:
            return "ERROR: " + sys.argv[4] + " is not recognized"

    #open and read file
    f = open(filename,"r",encoding='utf8')
    contents = f.read();
    f.close()
    contents = contents.replace("\n"," ")
    contents = contents.replace("!",".")
    contents = contents.replace("?",".")
    contents = contents.replace(".",". ")
    contents = contents.replace("-"," ")
    contents = contents.replace(","," ")
    contents = contents.replace(":"," ")
    contents = contents.replace("["," ")
    contents = contents.replace("]"," ")
    contents = contents.replace("("," ")
    contents = contents.replace(")"," ")
    wordList = contents.split(" ")
    while "" in wordList:
        wordList.remove("")

    #create dictionary.
    if not keep:
        map = {}
        map["$"] = []
        map["$"].append(re.sub("[^a-zA-Z]","",wordList[0]).lower())
    else:
        f = open(dest,'r')
        dictstr = f.read()
        f.close()
        map = dict(eval(dictstr))

    for i in range(len(wordList)-1):
        word  = wordList[i]
        cleanWord = re.sub("[^a-zA-Z]","",word).lower()
        if cleanWord not in map:
            map[cleanWord] = []

        next = wordList[i+1]
        cleanNext = re.sub("[^a-zA-Z]","",next).lower()
        if "." in word:
            map[cleanWord].append("$")
            map["$"].append(cleanNext);
        else:
            map[cleanWord].append(cleanNext)
    lastWord = wordList[len(wordList)-1]
    lastWord = re.sub("[^a-zA-Z]","",lastWord)
    if lastWord not in map:
        map[lastWord] = []
    map[lastWord].append("$")
    f = open(dest,'w')
    f.write(str(map))
    f.close()
    return "loaded from " + filename
