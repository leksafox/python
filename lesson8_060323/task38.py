'''Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

Задача 38: Дополнить телефонный справочник возможностью изменения 
и удаления данных. Пользователь также может ввести имя или фамилию, 
и Вы должны реализовать функционал для изменения и удаления данных'''

import os.path

tfn = "./phonebook.txt"

struct = {'lname':'Фамилия','fmane':'Имя','mnname':'Отчество','tel':'Телефон'}
data = []
print(struct)

def cleardata():
    data.clear()

def appenddata():
    temp = {}
    for k,tr in struct.items():
        temp[k] = input(f'Введите поле {tr}: ')
    data.append(temp)
    
def editdata(index):
    for k,tr in struct.items():
        text = input(f'Введите поле {tr} ({data[index][k]}): ')
        if len(text) > 0:
            data[index][k] = text
    
def deldata(index):
    data.pop(index)
    
def writetxtfile():
    file = open(tfn,"w")
    for i in range(len(data)):
        for k in data[i].keys():
            file.write(f'{k} = {data[i][k]}\n')
        file.write("\n")
    file.close()

def readfromtxt():
    if os.path.exists(tfn):
    #    print(f'Файл {tfn} найден')
        cleardata()
        file = open(tfn,"r")
        temp = {}
        for line in file:
            tt = ()
            if len(line) > 3:
                tt=line.split('=')
                temp[tt[0].strip()] = tt[1].strip()
            else:
                data.append({**temp})
    
        file.close()
    #else:
    #    print(f'Файл {tfn} не найден')
     
def printdata():
    for i in range(len(data)): 
        print(f'№: {i}')
        for k,tr in struct.items():
            print(f'{tr}: {data[i][k]}')
        print("----------")

def minihelp():           
    print("('s' - показать книгу, 'q' - выход, 'r' - отменить все изменения, 'а' - добавить запись, 'e' - редактировать, 'd' - удалить) ")

com = ''
minihelp()
readfromtxt()

while com != 'q':

    com = input("Введите команду управления телефонной книгой (h - help): ")

    if com == 'h':
        minihelp()
    
    elif com == 'r':
        readfromtxt()
        printdata()
    
    elif com == 'a':
        appenddata()
        printdata()
        
    elif com == 'd':
        deldata(int(input("Введите номер удаляемой ячейки: ")))
        printdata()
        
    elif com == 'e':
        editdata(int(input("Введите номер редактируемой ячейки: ")))
        print(data)
        printdata()

    elif com == 's':
        printdata()
    
    else:
        minihelp()        
     
writetxtfile()