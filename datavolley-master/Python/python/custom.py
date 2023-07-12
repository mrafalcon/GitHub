import datavolley


datavolley.init()

'''
code
codeCategory
DVS
Match
Teams
More
Comments
Set
PlayersH
PlayersV
Attack
Setter
Win
Reserve
Video
'''



def customClean():
    tempcodeCategory = datavolley.codeCategory
    for i in range(len(tempcodeCategory)):
        tempcodeCategory[i][3] = ''
    datavolley.megreCategory(tempcodeCategory)
    datavolley.splitCategory(datavolley.dvwGame)
    return 1

def customServeNum():
    tempcodeCategory = datavolley.codeCategory
    allgame = []
    allgame.clear()
    for i in range(1,7):
        for j in range(len(datavolley.dvwGame[i])):
            allgame.append(datavolley.dvwGame[i][j])
    lengame = len(allgame)
    c=1
    for i in range(len(tempcodeCategory)):
        if len(tempcodeCategory[i][0])>3:
            main = len(tempcodeCategory[i][0])
            adv = len(tempcodeCategory[i][1])
            ext = len(tempcodeCategory[i][2])
            simb = main+adv+ext
            if tempcodeCategory[i][0][3] == 'S':
                if (simb)>12 and (simb)<=15:
                    tempcodeCategory[i][2] = '{}{}'.format(tempcodeCategory[i][2], (15-(simb))*str('~'))
                elif (simb)>6 and (simb)<=12:
                    tempcodeCategory[i][1] = '{}{}'.format(tempcodeCategory[i][1], (12-(simb))*str('~'))
                    tempcodeCategory[i][2] = '{}{}'.format(tempcodeCategory[i][2], 3*str('~'))
                else:
                    tempcodeCategory[i][0] = '{}{}'.format(tempcodeCategory[i][0], (6-(simb))*str('~'))
                    tempcodeCategory[i][1] = '{}{}'.format(tempcodeCategory[i][1], 6*str('~'))
                    tempcodeCategory[i][2] = '{}{}'.format(tempcodeCategory[i][2], 3*str('~'))
                tempcodeCategory[i][3] = '{}{}'.format(tempcodeCategory[i][3], str('c'))
            
    datavolley.megreCategory(tempcodeCategory)
    datavolley.splitCategory(datavolley.dvwGame)
    return 1