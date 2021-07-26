from random import *
from math import sqrt

#Функция для формирования строки и удаления лишних символов
def predtext(s):
    s = s.lower()#Выравнивание строки - все прописные.
    s = s.replace('.', 'тчк') # Если в сообщении попадется точка, 
                              #она заменется на тчк
    s = s.replace(',', 'зпт') # Если в сообщении попадется запятая, 
                              #она заменется на зпт
    s = s.replace('-', 'тире') # Если в сообщении попадется тире, 
                               # символ заменется на тире
    s = s.replace('!', 'вскзн') # Если в сообщении попадется !, 
                            # символ заменется на вск\
    s = s.replace(':', 'двтч') # Если в сообщении попадется :, 
                            # символ заменется на двтчк
    s = s.replace("'", '') # Если в сообщении попадется ' при 
                            #выгрузке из файла, символ удалим
    s = s.replace('[', '') # Если в сообщении попадется [ при 
                            #выгрузке из файла, символ удалим
    s = s.replace(']', '') # Если в сообщении попадется ] при 
                            #выгрузке из файла, символ удалим
    s = s.replace(' ', 'прбл') # Если в сообщении попадется пробел
                            #при выгрузке из файла, символ заменим на пробел
    s = s.replace('\\n', 'слэш') # Если в сообщение разделяется, 
                                #то и это заменим на слэщ
    s = s.replace('слэшзпт', 'слэш')
    return s 

alph_ru ='абвгдежзийклмнопрстуфxцчшщъыьэюя'
#Функция хеширования
def hash_kvadr(m1):
    h = 0
    for i in m1:
        h1 = h
        h = ((h1+alph_ru.index(i)+1)*(h1+alph_ru.index(i)+1)) % 11
    return h


def NOD(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def vz(D,M):
    if NOD(D,M) == 1:
        return False
    else:
        return True


#Алгоритм проверки числа: простое ли оно?
def prostoy(n):
    if n < 2:
        return False
    if n == 2:
        return True
    limit = sqrt(n)
    i = 2
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    #return True

def get_vz(P):
    k = randrange(2, (P-1), 1)
    while vz(k,(P-1)) and k != 1:
        k = randrange(2, (P-1), 1)
    return k


#Проверка вводимого числа P на простоту
def vv_P(): 
    n = int(input('Введите открытый ключ P: '))
    if ( prostoy(n)== True):
        return n
    else:
        while(prostoy(n)== False):
            n = int(input('Введите открытый ключ P: '))
    return n

#Проверка вводимого числа X :
# 1 < Х ≤ (Р-1),
def vv_X(p): 
    x = int(input('Введите секретный ключ X: '))
    if (x > 1 and x <= (p-1)) :
        return x
    else:
        while(x < 1 and x > (p-1)):
            x = int(input('Введите секретный ключ X: '))
    return x

#Проверка вводимого числа G :
# G < Р
def vv_G(p): 
    g = int(input('Введите открытый ключ G: '))
    if (g < p) :
        return g
    else:
        while(g > p):
            g = int(input('Введите открытый ключ G: '))
    return g

#Работа с файлами
file = open("otkrutuytext.txt", "r")#открыть файл для чтения
data = file.readlines() #читать все строки
file.close()
m1 = str(data)
print("Ваша строка:  ", m1)
m1 = predtext(str(data))
#Выводим значения на экран для собственной проверки
print("Преобразованная строка: ", m1)

P= vv_P()
X = vv_X(P)
G= vv_G(P)
Y = (G  ** X) % P
print("Значение Y: ", Y)
kol = int(input('Введите количество k: '))
u = 0
list_k = []
print("Возможные значения k относительно введенного количества: \n" )
while (u != kol):
    k = get_vz(P)
    print("K[", u+1, "]=", k ,"\n")
    list_k.append(k)
    u += 1

m = hash_kvadr(m1)
a = 0
it_k = int(input('Введите значение k, которое мы возьмем для дальнейшего преобразования: '))
a = G ** (list_k[it_k-1]) % P

b = 0
while m != ((X * a + (list_k[it_k-1]) * b) % (P-1)):
    b += 1

print('Цифровая подпись S: ', (a,b))
a1 = 0
a1 = (Y ** a) * (a ** b) % P

a2 = 0
a2 = G ** m % P

print('A1 = ', a1, 'A2 = ', a2)
if a1 == a2:
    print('Значения совпали. Подпись верна')
else:
    print('Значения не совпали. Подпись не верна')

#Работа с файлами - запись хеша
file = open("hesh.txt", "w")
file.writelines('Хеш вашего сообщения: '+str(m))
file.seek(0)
file.close()

#Работа с файлами - запись подписи
file = open("podpis.txt", "w")
file.writelines('Ваша цифровая подпись S: (a ='+str(a) + '; b ='+str(b) + ')')
file.seek(0)
file.close()

#Работа с файлами - запись открытых ключей
file = open("otkr_kl.txt", "w")
str1 = 'Открытый ключ Y: '+str(Y)
file.writelines(str1)
file.seek(0)
file.close()

#Работа с файлами - запись секретного ключа
file = open("sekr_kl.txt", "w")
str2 = 'Секретный ключ X: '+str(X)
file.writelines(str2)
file.seek(0)
file.close()