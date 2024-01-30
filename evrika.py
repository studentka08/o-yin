from random import randint
_='_'
oyin = []
bomba = '💣'

for i in range(10):
    joy = randint(0,4)
    row = [_, _, _, _, _,]
    row[joy]=bomba
    oyin.append(row)


qator,ustun = 9,3
oyin[qator][ustun] = '🟢'

while qator!=0:
    for row in oyin:
        for i in row:
            print(i, end='  ')
        print('\n')
    print("""
         w 
    a        d
          s
""")
    yurish = input(':')
    oyin[qator][ustun] = '_'
    if yurish=='w':
        qator -= 1
    elif yurish=='a':
        ustun-= 1
    elif yurish =='s':
        qator += 1
    elif yurish=='d':
        ustun+= 1
    if oyin[qator][ustun]==bomba:
        break

    oyin[qator][ustun] = '🟢'

for row in oyin:
    for i in row:
        print(i,end='  ')
    print('\n')

if oyin[qator][ustun]==bomba:
    print('siz yutqazdiz')
elif '🟢' in oyin[0]:
    print('siz yutdiz')
