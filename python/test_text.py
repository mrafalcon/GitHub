import os
import pandas as pd

#from progress.bar import Bar

cwd = os.getcwd()
cwd
os.chdir("/Users/andreisokolov/Documents/GitHub/GitHub/python/")
os.listdir('.')

content_array = []

file = "test_text.txt"


with open(file, "r", encoding= "cp1251") as file:
    content = file.read()
content = content.split('\n')
#bar = Bar('Processing', max=len(content))
for i in range(len(content)):
    content_array.append(content[i].split('.'))
    #bar.next()
#bar.finish()


print(content_array)