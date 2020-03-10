a=input("Введите 1-ю строку: ")
b=input("Введите 2-ю строку: ")

c=len(a)
d=len(b)

i=0
while i != d-1:
    if b[i] in a:
        i=i+1
    elif b[i] == '*':
        i=i+1
    else:
        break
if i+1 == d:
    stat1='GOOD'
else:
    stat1='BAD'


if stat1 == 'GOOD':
    for i in range(c):
        if a[i]!=b[i]:
            if b[i] == '*':
                stat2='GOOD'
                break
            else:
                stat2='BAD'
                break
        if i == (c-1):
            stat2='GOOD'
else:
    stat2='BAD'
    
            
if stat2 == 'GOOD':
    i=1
    while i!=c+1 or i!=d+1:
        if a[c-i] == b[d-i] or b[d-i]=='*':
            stat34='GOOD'
            if b[d-i] == '*':
                break
            else:
                i=i+1
        else:
            stat34='BAD'
            break
else:
    stat34='BAD'   

if stat1==stat2==stat34=='GOOD':
    print('OK')
else:
    print('KO')
    
input('Нажмите Enter для выхода')
