while True:
    nb = input('Введите число: ')
    nb = nb.upper()
    if nb.isalnum():
        break
    else:
        print('Вы ввели неправильное значение!')
        
while True:
    baseSrc = int(input('Введите систему счисления введенного числа (2-36): '))
    if baseSrc in range(2,36):
        break
    else:
        print('Вы ввели неправильное значение!')

while True:
    baseDst = int(input('Введите систему счисления, в которую необходимо перевести (2-36): '))
    if baseSrc in range(2,36):
        break
    else:
        print('Вы ввели неправильное значение!')

slov={
    10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F',
    16:'G', 17:'H', 18:'I', 19:'J', 20:'K', 21:'L',
    22:'M', 23:'N', 24:'O', 25:'P', 26:'Q', 27:'R',
    28:'S', 29:'T', 30:'U', 31:'V', 32:'W', 33:'X',
    34:'Y', 35:'Z'}

def get_key(slov, value): # Ф-я находит ключ по значению
    for k, v in slov.items():
        if v == value:
            return k


def convert_to_dec1(n,c): #Ф-я переводит из любого основания в десятичную, где n-число, с-основание
    res=0
    for i in range(len(n)-1,-1,-1):
        if n[i] in slov.values():
            res = res + (int(get_key(slov,n[i])))*(c**((len(n)-1)-i))
        else:
            res = res + (int(n[i])*(c**((len(n)-1)-i)))
    return res

def convert_dec(n,c): #Ф-я переводит число из десятичной в любую другую
    res=''
    while int(n) > 0:
        if int(n)%c in slov:
            res = slov[int(n)%c]+res
        else:
            res = str(int(n)%c)+res
        n = int(n)// c
    print(res)
    

if baseSrc == 10 :
    convert_dec(nb,baseDst)
else:
    nb1 = convert_to_dec1(nb,baseSrc)
    convert_dec(nb1,baseDst)
input('Нажмите Enter для выхода')
