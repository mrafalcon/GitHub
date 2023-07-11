code = ['*10AT#X8~95AH2~1']
code_list = []
for i in range(len(code)):
    code_list.append(list(code[i]))

print(code[0]+2)
print(code[0][0:1])
print(code[0][0:1] == '*1')
print(code[0][0:1] == str('*1'))
print(code[0][6:12])
print(code[0][12:15])
print(code[0][15:20])