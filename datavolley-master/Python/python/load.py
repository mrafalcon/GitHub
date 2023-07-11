import os
from tabulate import tabulate
import re

def init():
    global dvwGame, technical, game, set1, set2, set3, set4, set5, set6, code
    technical = []
    game = []
    set1 = []
    set2 = []
    set3 = []
    set4 = []
    set5 = []
    set6 = []
    dvwGame = [technical, set1, set2, set3, set4, set5, set6]
    code = []

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



def importFile(file):
    global statusLoad
    statusLoad = False
    technical.clear()
    game.clear()
    set1.clear()
    set2.clear()
    set3.clear()
    set4.clear()
    set5.clear()
    set6.clear()
    code.clear()
    lcount = 0
    found = False
    with open(file, "r", encoding='latin-1') as f:
        content = f.read()
        content = content.split('\n')
        pos0 = findWord("[3SCOUT]", content)
        pos1 = findWord("**1set", content)
        pos2 = findWord("**2set", content)
        pos3 = findWord("**3set", content)
        pos4 = findWord("**4set", content)
        pos5 = findWord("**5set", content)
        pos6 = findWord("**6set", content)
    

 
        for i in range (pos0):
            technical.append(content[i])
        for i in range (pos0, len(content)):
            game.append(content[i])
        for i in range (pos0, pos1):
            set1.append(content[i])
        for i in range(len(set1)):
            set1[i] = str(set1[i]).split(';')
        for i in range (pos1, pos2):
            set2.append(content[i])
        for i in range(len(set2)):
            set2[i] = str(set2[i]).split(';')
        for i in range (pos2, pos3):
            set3.append(content[i])
        for i in range(len(set3)):
            set3[i] = str(set3[i]).split(';')
        if pos4 > 0:
            for i in range (pos3, pos4):
                set4.append(content[i])
            for i in range(len(set4)):
                set4[i] = str(set4[i]).split(';')
        if pos5 > 0:
            for i in range (pos4, pos5):
                set5.append(content[i])
            for i in range(len(set5)):
                set5[i] = str(set5[i]).split(';')
        if pos6 > 0:
            for i in range (pos5, pos6):
                set6.append(content[i])
            for i in range(len(set6)):
                set6[i] = str(set6[i]).split(';')
        
        for i in range(1,6):
            for j in range(len(dvwGame[i])):
                code.append(dvwGame[i][j][0])
        for i in range(len(code)):
            code[i] = re.split(r'\~+', code[i])
    if len(code) > 0:
        statusLoad = True
