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

def customServe():
    tempcodeCategory = datavolley.codeCategory
    allgame = []
    allgame.clear()
    for i in range(1,7):
        for j in range(len(datavolley.dvwGame[i])):
            allgame.append(datavolley.dvwGame[i][j])
    count = 1
    currentPlayer = 0
    scoreDec = '00'
    for i in range(len(tempcodeCategory)):
        if len(tempcodeCategory[i][0])==7:
            if tempcodeCategory[i][0][1] == 'p':
                scoreDec = tempcodeCategory[i][0][2]+tempcodeCategory[i][0][5]
        
        if len(tempcodeCategory[i][0])>3:
            main = len(tempcodeCategory[i][0])
            adv = len(tempcodeCategory[i][1])
            ext = len(tempcodeCategory[i][2])
            simb = main+adv+ext
            if tempcodeCategory[i][0][3:6] == 'set':
                currentPlayer = 0
                scoreDec = '00'
            if tempcodeCategory[i][0][3] == 'S':
                if tempcodeCategory[i][0][0:3] != currentPlayer:
                    currentPlayer = tempcodeCategory[i][0][0:3]
                    count = 1
                if (simb)>12 and (simb)<=15:
                    tempcodeCategory[i][2] = '{}{}'.format(tempcodeCategory[i][2], (15-(simb))*str('~'))
                elif (simb)>6 and (simb)<=12:
                    tempcodeCategory[i][1] = '{}{}'.format(tempcodeCategory[i][1], (12-(simb))*str('~'))
                    tempcodeCategory[i][2] = '{}{}'.format(tempcodeCategory[i][2], 3*str('~'))
                else:
                    tempcodeCategory[i][0] = '{}{}'.format(tempcodeCategory[i][0], (6-(simb))*str('~'))
                    tempcodeCategory[i][1] = '{}{}'.format(tempcodeCategory[i][1], 6*str('~'))
                    tempcodeCategory[i][2] = '{}{}'.format(tempcodeCategory[i][2], 3*str('~'))
                tempcodeCategory[i][3] = '{}{}'.format(tempcodeCategory[i][3], str(count))
                count = count + 1

                if tempcodeCategory[i][1][4] in set(('7','8','9')):
                    tempcodeCategory[i][3] = '{}{}'.format(tempcodeCategory[i][3], str('U'))

                if allgame[i][8] in set(('1', '2', '3', '4')):
                    if scoreDec in set(('22', '33', '44', '55', '66', '77', '88', '99')):
                        tempcodeCategory[i][3] = '{}{}'.format(tempcodeCategory[i][3], str('E'))
                elif allgame[i][8] == '5':
                    if scoreDec in set(('11', '22', '33', '44', '55', '66', '77', '88', '99')):
                        tempcodeCategory[i][3] = '{}{}'.format(tempcodeCategory[i][3], str('E'))

                

            
    datavolley.megreCategory(tempcodeCategory)
    datavolley.splitCategory(datavolley.dvwGame)
    return 1