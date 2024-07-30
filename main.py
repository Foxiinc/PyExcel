import pandas as pd
import os 
path_file = input('Введите название файла:\n')

#Данные из .csv
filename, filetype = os.path.splitext(path_file) 
print(filetype)
if filetype == '.xlsx':
    #Данные из столбца excel    
    excel = pd.read_excel(path_file)#Название таблицы
    column = excel.iloc[:,0].tolist()#Опредяем номер столбца и записываем данные в лист names
    #Данные из строки excel
    line = excel.iloc[0].tolist()#Определям номер строки и записываем её в строку
elif filetype == "csv":
    print('CS')


    
    


