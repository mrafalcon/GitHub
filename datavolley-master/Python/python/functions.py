import os

def findWord(word, content):
    lcount = 1
    found = False
    for i in range(len(content)):
            if word in content[i]: # If word is in line
                found = True
                break
            else:
                lcount += 1
    if found:
        return lcount
    else:
        return 0