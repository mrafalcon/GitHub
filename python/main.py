import os
import pandas as pd

cwd = os.getcwd()
cwd

os.chdir(r"C:\Users\gz1\Documents\Соколов\Расчет Потери линейного времени\2023\06")

file = os.listdir('.')
xl = pd.ExcelFile(file[0])

# Load a sheet into a DataFrame by name: df1

df1 = xl.parse(xl.sheet_names[0])

print (df1)