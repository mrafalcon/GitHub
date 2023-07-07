import os

def init():
    global technical, game, set1, set2, set3, set4, set5
    technical = []
    game = []
    set1 = []
    set2 = []
    set3 = []
    set4 = []
    set5 = []

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
#        print(lcount)
        return lcount
    else:
#        print(0)
        return 0



def importFile(dir, file):
    cwd = os.getcwd()
    os.chdir(dir)
    lcount = 0
    found = False
    with open(file, "r") as f:
        content = f.read()
        content = content.split('\n')
        pos0 = findWord("[3SCOUT]", content)
        pos1 = findWord("**1set", content)
        pos2 = findWord("**2set", content)
        pos3 = findWord("**3set", content)
        pos4 = findWord("**4set", content)
        pos5 = findWord("**5set", content)

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
#    return technical, game, set1, set2, set3, set4, set5
