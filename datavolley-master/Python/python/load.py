import os
from tabulate import tabulate
import re

def init():
    global dvwGame, technical, game, set1, set2, set3, set4, set5, set6, code, codeCategory, DVS,Match,Teams, More , Comments , Set, PlayersH , PlayersV , Attack , Setter , Win , Reserve , Video 
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
    codeCategory = []
    DVS = []
    Match = []
    Teams = []
    More = []
    Comments = []
    Set = []
    PlayersH = []
    PlayersV = []
    Attack = []
    Setter = []
    Win = []
    Reserve = []
    Video = []


def importFile(file):
    global statusLoad, text_encoding
    statusLoad = False

    with open(file, "r", encoding='cp1251') as f:
        content = f.read()
        content = content.split('\n')
        text_encoding = 'cp'+str(content[findWord("[3MATCH]", content)]).split(';')[8]

    if text_encoding != 'cp1251':
        with open(file, "r", encoding=text_encoding) as f:
            content = f.read()
            content = content.split('\n')
    
    readFile(content)
        
    if len(code) > 0:
        statusLoad = True

def readFile(content):

    technical.clear()
    game.clear()
    set1.clear()
    set2.clear()
    set3.clear()
    set4.clear()
    set5.clear()
    set6.clear()
    code.clear()
    codeCategory.clear()
    DVS.clear()
    Match.clear()
    Teams.clear()
    More.clear()
    Comments.clear()
    Set.clear()
    PlayersH.clear()
    PlayersV.clear()
    Attack.clear()
    Setter.clear()
    Win.clear()
    Reserve.clear()
    Video.clear()


    posDVS = findWord("[3DATAVOLLEYSCOUT]", content)
    posMatch = findWord("[3MATCH]", content)
    posTeams = findWord("[3TEAMS]", content)
    posMore = findWord("[3MORE]", content)
    posComments = findWord("[3COMMENTS]", content)
    posSet = findWord("[3SET]", content)
    posPlayersH = findWord("[3PLAYERS-H]", content)
    posPlayersV = findWord("[3PLAYERS-V]", content)
    posAttack = findWord("[3ATTACKCOMBINATION]", content)
    posSetter = findWord("[3SETTERCALL]", content)
    posWin = findWord("[3WINNINGSYMBOLS]", content)
    posReserve = findWord("[3RESERVE]", content)
    posVideo = findWord("[3VIDEO]", content)
    pos0 = findWord("[3SCOUT]", content)
    pos1 = findWord("**1set", content)
    pos2 = findWord("**2set", content)
    pos3 = findWord("**3set", content)
    pos4 = findWord("**4set", content)
    pos5 = findWord("**5set", content)
    pos6 = findWord("**6set", content)
    
     
    for i in range (pos0):
        technical.append(content[i])

    for i in range (posDVS, posMatch):
        DVS.append(content[i])
    for i in range(len(DVS)):
        DVS[i] = str(DVS[i]).split(':')

    for i in range (posMatch, posTeams):
        Match.append(content[i])
    for i in range(len(Match)):
        Match[i] = str(Match[i]).split(';')

    for i in range (posTeams, posMore):
        Teams.append(content[i])
    for i in range(len(Teams)):
        Teams[i] = str(Teams[i]).split(';')

    for i in range (posMore, posComments):
        More.append(content[i])
    for i in range(len(More)):
        More[i] = str(More[i]).split(';')

    for i in range (posComments, posSet):
        Comments.append(content[i])
    for i in range(len(Comments)):
        Comments[i] = str(Comments[i]).split(';')

    for i in range (posSet, posPlayersH):
        Set.append(content[i])
    for i in range(len(Set)):
        Set[i] = str(Set[i]).split(';')

    for i in range (posPlayersH, posPlayersV):
        PlayersH.append(content[i])
    for i in range(len(PlayersH)):
        PlayersH[i] = str(PlayersH[i]).split(';')

    for i in range (posPlayersV, posAttack):
        PlayersV.append(content[i])
    for i in range(len(PlayersV)):
        PlayersV[i] = str(PlayersV[i]).split(';')

    for i in range (posAttack, posSetter):
        Attack.append(content[i])
    for i in range(len(Attack)):
        Attack[i] = str(Attack[i]).split(';')

    for i in range (posSetter, posWin):
        Setter.append(content[i])
    for i in range(len(Setter)):
        Setter[i] = str(Setter[i]).split(';')

    for i in range (posWin, posReserve):
        Win.append(content[i])
    for i in range(len(Win)):
        Win[i] = str(Win[i]).split(';')

    for i in range (posReserve, posVideo):
        Reserve.append(content[i])
    for i in range(len(Reserve)):
        Reserve[i] = str(Reserve[i]).split(';')

    for i in range (posVideo, pos0):
        Video.append(content[i])
    for i in range(len(Video)):
        Video[i] = str(Video[i]).split(';')


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
        if code[i][0:2] == '*p' or code[i][0:2] ==  'ap' or code[i][0:2] == '*P' or code[i][0:2] == 'aP' or code[i][0:2] ==  '*z' or code[i][0:2] ==  'az' or code[i][0:2] ==  '**' :
            codeCategory.append([code[i],'','',''])
        else:
            codeCategory.append([code[i][0:6],code[i][6:12],code[i][12:15],code[i][15:20]])

'''
[0:6] - main code
[6:12] - advanced code
[12:15] - externed code
[15:20] - custom code
'''


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

