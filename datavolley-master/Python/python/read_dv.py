import os
import datavolley
import functions



def importFile(file):
    global statusLoad, text_encoding
    statusLoad = False

    with open(file, "r", encoding='cp1251') as f:
        content = f.read()
        content = content.split('\n')
        text_encoding = 'cp'+str(content[functions.findWord("[3MATCH]", content)]).split(';')[8]

    if text_encoding != 'cp1251':
        with open(file, "r", encoding=text_encoding) as f:
            content = f.read()
            content = content.split('\n')
    
    datavolley.readFile(content)
        
    if len(datavolley.code) > 0:
        statusLoad = True
