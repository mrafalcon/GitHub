import os
import datavolley
import read_dv
import datetime

#read_dv.init()

def writeFile(filepath):
    if datetime.datetime.now().month > 9:
        month = str(datetime.datetime.now().month)
    else:
        month = '0'+str(datetime.datetime.now().month)
    if datetime.datetime.now().day > 9:
        day = str(datetime.datetime.now().day)
    else:
        day = '0'+str(datetime.datetime.now().day)
    
    if datetime.datetime.now().hour > 9:
        hour = str(datetime.datetime.now().hour)
    else:
        hour = '0'+str(datetime.datetime.now().hour)
    if datetime.datetime.now().minute > 9:
        minute = str(datetime.datetime.now().minute)
    else:
        minute = '0'+str(datetime.datetime.now().minute)
    if datetime.datetime.now().second > 9:
        second = str(datetime.datetime.now().second)
    else:
        second = '0'+str(datetime.datetime.now().second)

    datavolley.dvwGame[0][8] = datavolley.dvwGame[0][8].split(' ')[0] + ' ' + day + '/' + month + '/' +str(datetime.datetime.now().year)  + ' ' + hour + '.' + minute + '.' + second

    with open(filepath, "w", encoding=read_dv.text_encoding) as f:
                for item in datavolley.technical:
                    f.write("%s\n" % str(item))
                for item in datavolley.dvwGame[1]+datavolley.dvwGame[2]+datavolley.dvwGame[3]+datavolley.dvwGame[4]+datavolley.dvwGame[5]+datavolley.dvwGame[6]:
                    f.write( ";".join(str(a) for a in item) +"\n")