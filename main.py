import sys
from stats import *

try:
    bookPath = sys.argv[1]
except:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def getBookText(c):
    with open(c) as f:
        contents = f.read()
    return contents

def main():
    numWord = wordCount(getBookText(bookPath))
    charDict = charCount(getBookText(bookPath))
    sortedList = sortDict(charDict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookPath}...")
    print("----------- Word Count ----------")
    print(f"Found {numWord} total words")
    print("--------- Character Count -------")
    for i, k in enumerate(sortedList):
        if sortedList[i]["char"].isalpha():
            print(sortedList[i]["char"] + ": " + str(sortedList[i]["num"]))
    print("============= END ===============")

main()