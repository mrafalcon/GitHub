import os
import pandas as pd

cwd = os.getcwd()
cwd
os.chdir(r"C:\Users\gz1\Downloads\GitHub\GitHub\python")
os.listdir('.')

content_array = []

file = 'test_text.txt'
with open(file, "r") as file:
    content = file.read()
content = content.split('\n')
for i in range(len(content)):
    content_array.append(content[i].split('.'))


print(content_array)