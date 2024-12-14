import random

#задание1 - угадать число
rand = random.randint(1,10)
popit = 0

print("Ugadai chislo")
while True:
  n = int(input("chislo "))
  if (rand == n):
    print("Vi viygrali za ", popit, "количество попыток")
    break
  else:
    print("Ne ugadali")
    popit += 1;
    
#задание2 - у меня вскипели мозги, если честно  
mass = input("Bukvi: ").lower().split(' ')
result = []
temp = []

for i in range(len(mass)):
    if len(temp) == 0 or mass[i] == temp[0]:
        temp.append(mass[i])  
    else:
        result.append(temp)  
        temp = [mass[i]]

if len(temp) > 0:
    result.append(temp)  

final = []  
seen = []  

for item in mass:
    if item not in seen:  
        seen.append(item)  
        gruppa = []
        for i in mass:
            if i == item:
                gruppa.append(i)
        final.append(gruppa)

print(final)

#задание3 - игра в очко
mast = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 2, 'Q': 3, 'K': 4, 'A': 11}
random.shuffle(mast)
ochki = 0

while True:
    answer = input("у - vzat card\nn - zakonchit game\n")
    
    if answer == 'n':
        print("You have", ochki, "ochkov.  Buy")
        break
    elif answer == 'y':
        card = mast.pop()
        ochki += values[card]  
        
        print("Your card:", card)
        print("Your ochki:", ochki)
        
        if ochki > 21:
            print("You loser! You have bolshe 21 ochkkov")
            break
        elif ochki == 21:
            print("Happy time! You winner! Buy")
            break
    else:
        print("y!!!!!! or n!!!!!!!!")
