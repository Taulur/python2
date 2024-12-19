# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Get started with interactive Python!
# Supports Python Modules: builtins, math,pandas, scipy 
# matplotlib.pyplot, numpy, operator, processing, pygal, random, 
# re, string, time, turtle, urllib.request
import random

#1 
rand = random.randint(1,10)
p = 1
print("Угадай число")
while True:
  num = int(input("Число "))
  if (rand == num):
    print("Вы выиграли за", p, "попыток")
    break
  else:
    print("Вы не угадали, попробуйте ещё раз!3")
    p += 1;
    if (num > rand): print("Загаданое число меньше")
    else: print("Загаданное число больше")
    
#2
m = input("Буквы: ").lower().split(' ')
result = []
seen = set() 

for item in m:
    if item not in seen:  
        seen.add(item)  
        group = []  
        for other in m:
            if other == item: 
                group.append(other)
        result.append(group) 

print(result)
#3 
mast = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 2, 'Q': 3, 'K': 4, 'A': 11}
random.shuffle(mast)
c = 0

while True:
    answer = input("у - Взять карту\nn - Закончить игру\n")
    
    if answer == 'n':
        print("У тебя", c, "очков\n")
        break
    elif answer == 'y':
        card = mast.pop()
        c+= values[card]  
        
        print("Твоя карта:", card)
        print("Твои очки:", c)
        
        if c > 21:
            print("Ты проиграл. У тебя больше 21 очков :(")
            break
        elif c == 21:
            print("Ура ты крутой, ТЫ ВЫИГРАЛ!!! Возьми с полки пирожок :)")
            break
    else:
        print("Напиши y или n")
