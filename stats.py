def wordCount(content):
    return len(content.split())

def charCount(content):
    charDict = dict()
    for char in content.lower():
        charDict[char] = charDict.get(char, 0) + 1
    return charDict

def getDictNum(sd):
    return sd["num"]

def sortDict(d):
    sd = []
    for k in d:
        sd.append({"char": k, "num": d[k]})
    sd.sort(key=getDictNum, reverse=True)
    return sd
