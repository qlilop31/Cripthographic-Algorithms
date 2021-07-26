import sys
from math import gcd
import random
from textwrap import wrap
from sympy.ntheory import totient

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']


def euler(n):  # функция эйлера
    r = n
    i = 2
    while i*i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            r -= r//i
        else:
            i += 1
    if n > 1:
        r -= r//n
    return r


def completeNum(_string, num):  # добавляем 0 в начало числа, если его длина меньше указанной
    while len(_string) < num:
        _string = "0" + _string

    return _string


def getDivisorsNumber(_num):  # найти все делители числа
    divisorsList = list()
    for i in range(1, _num+1):
        if (_num % i) == 0:
            divisorsList.append(i)

    return divisorsList


def errorMessage(p_q):
    testList = [1, p_q]
    if getDivisorsNumber(p_q) != testList:
        print("ваше число не простое, попробуйте ещё раз")
        sys.exit()


def errorMessageN(_maxElem, _n):
    if _n < _maxElem:
        print("Вы выбрали слишком маленькие значения P и Q, попробуйте ещё раз.")
        sys.exit()


def findD(_N_euler, num, _e):
    degree = euler(_N_euler)-1
    _d = (num * _e**degree) % _N_euler
    return _d


def keyGenerate(_p, _q):
    _N = _p * _q
    N_euler = (_p - 1) * (_q - 1)

    randomList = list(range(2, 10000))
    random.shuffle(randomList)

    _E = 0  # выбирается случайное целое число E, взаимно простое с φ(N)
    for x in randomList:
        if gcd(x, N_euler) == 1:
            _E = x
            break

    _D = findD(N_euler, 1, _E)  # высчитываем D

    return _D, _E, _N


def textToNum(_string):
    numList = list()
    for letter in _string:
        numList.append(ord(letter))

    return numList


"""def textToNum(_string):
    numList = list()
    for letter in _string:
        numList.append(alphabet.index(letter)+1)

    return numList"""


def enc(_stringCodeList, _e, _n):
    _newString = ""
    for Mi in _stringCodeList:
        Ci = Mi**_e % _n
        _newString += completeNum(str(Ci), len(str(_n)))

    return _newString


def dec(_newString, _n, _d):
    _newList = wrap(_newString, len(str(_n)))
    _newString = ""
    for Ci in _newList:
        Mi = int(Ci)**_d % _n
        _newString += chr(Mi)
        # _newString += alphabet[Mi-1]

    return _newString


#####################################################################


string = input("Введите текст: ")
stringCodeList = textToNum(string)

p = int(input("Введите P (простое число): "))
errorMessage(p)
q = int(input("Введите Q (простое число): "))
errorMessage(q)

D, E, N = keyGenerate(p, q)

errorMessageN(max(stringCodeList), N)

# print("Коды: ", stringCodeList)

newString = enc(stringCodeList, E, N)
print("Текст в зашифрованном виде: ", newString)

newString = dec(newString, N, D)
print("Текст в расшифрованном виде: ", newString)








