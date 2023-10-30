import os
import datetime


now = datetime.datetime.now()
#Main menu array
menu = ["Добавить заметку","Удалить заметку","Вывести заметки","Изменить заметку","Стоп","Выбрать по дате"]




#Function to clear console
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


#Function to navigate in main menu


#Function to print
def removeNotes():
    clear_console()
    printNote()
    id = int(input("Выберите id для удаления:"))
    count = 0
    arraytemp = []
    with open("mynote.txt","r",encoding="utf-8")as file:
        found = False  
        for line in file:
            if line.startswith("("):
                count += 1
                if id == count:
                    found = True
                else:
                    found = False
            if not found:
                arraytemp.append(line)
            

    with open("mynote.txt","w",encoding="utf-8")as file2:
        for line in arraytemp:
            file2.write(line)
    


#Function to add
def addNote(choice):
    title = input("Введите заголовок:")
    text = input("Введите текс:")
    with open("mynote.txt","a",encoding="utf-8")as file:
        file.write(f"({now})" + "\n" + f"[{title}]" + "\n")
        file.write(text + "\n")


#Function to print
def printNote():
    clear_console()
    id = 1
    with open("mynote.txt", "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("["):
                print(f"[{id}]")
                id += 1
            print(line)

def printWithData():
    year = input("Год:")
    mounth = input("Месяц:")
    day = input("День:")
    arraytemp = []
    counter = 0
    currentline = None
    dataline = None
    textline = None
    with open("mynote.txt","r",encoding="utf-8")as file:
        for line in file:
            if line.startswith(f"{year}") or line.startswith(f"{year}"+"-"+f"{mounth}") or line.startswith(f"{year}"+"-"+f"{mounth}" + "-" + f"{day}"):
                print(line)
        while(counter<2):
            print(line)
            counter += 1
            
                
                
        # print(arraytemp)
                

        
def changeNote():
    clear_console()
    printNote()
    id = int(input("Выберите id для изменения:"))
    clear_console()
    newtitle = input("Введите новый заголовок:")
    newtext = input("Введите новый текст:")
    count = 0
    arraytemp = []
    with open("mynote.txt","r",encoding="utf-8")as file:
        found = False  
        for line in file:
            if line.startswith("["):
                count += 1
                if id == count:
                    found = True
                else:
                    found = False
            if not found:
                arraytemp.append(line)

    with open("mynote.txt","w",encoding="utf-8")as file2:
        file2.write(f"[{newtitle}]"+"\n" + f"{now}" + "\n" + f"{newtext}" + "\n")
        for line in arraytemp:
            file2.write(line)
            



#Main function
def selectedchoice(choice):
    if(choice > 0 and choice < 7):
        if(choice == 1):
            addNote(choice)
        if(choice == 2):
            removeNotes()
        if(choice == 3):
            printNote()
        if(choice == 4):
            changeNote()
        if(choice == 6):
            printWithData()
        
                
    else:
        clear_console()
        print("Нет такого выбора")




#Main page
while(True):
    print(" | ".join(menu))
    choice = int(input("Ваше действие(1-6):"))
    clear_console()
    selectedchoice(choice)
    if(choice == 5):
        break

    