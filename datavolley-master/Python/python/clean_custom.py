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