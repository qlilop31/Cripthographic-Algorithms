import re
import copy
import sys 
# Регистры
reg_x_length = 19
reg_y_length = 22
reg_z_length = 23

key_one = ""
reg_x = []
reg_y = []
reg_z = []

def loading_registers(key): #загружает регистры, используя в качестве параметра 64-разрядный ключ
    i = 0
    while(i < reg_x_length): 
        reg_x.insert(i, int(key[i])) #берет первые 19 элементов из ключа
        i = i + 1
        j = 0
        p = reg_x_length
    while(j < reg_y_length): 
        reg_y.insert(j,int(key[p])) #берет следующие 22 элемента из ключа
        p = p + 1
        j = j + 1
        k = reg_y_length + reg_x_length
        r = 0
    while(r < reg_z_length): 
        reg_z.insert(r,int(key[k])) #берет последние 23 элемента из ключа
        k = k + 1
        r = r + 1

def set_key(key): #устанавливает ключ и загружает регистры если он содержит 0 и 1 и если это ровно 64 бита  
    if(len(key) == 64 and re.match("^([01])+", key)):
        key_one=key
        loading_registers(key)
        return True
    return False

def to_binary(plain): # Преобразование открытого текста в двоичный формат
    binary = list(map(lambda x: "{0:b}".format(ord(x)).zfill(11), plain))
    return binary

def get_majority(x,y,z): # Получает большинство, суммируя значения x,y и z, и если оно больше 1 (например, два 1 и один 0), он возвращает большинство (1). В противном случае, если это два 0 и один 1, большинство возвращается как 0.
    return (x&y | x&z | y&z) # Функция F

def get_keystream(length): #Вычисление ключевого потока с помощью XOR соответствующих индексов
    reg_x_temp = copy.deepcopy(reg_x)
    reg_y_temp = copy.deepcopy(reg_y)
    reg_z_temp = copy.deepcopy(reg_z)
    keystream = []
    i = 0
    while i < length:
        majority = get_majority(reg_x_temp[7], reg_y_temp[9], reg_z_temp[9])
        if reg_x_temp[7] == majority: 
            new = reg_x_temp[0] ^ reg_x_temp[13] ^ reg_x_temp[16] ^ reg_x_temp[17] ^ reg_x_temp[18]
            reg_x_temp_two = copy.deepcopy(reg_x_temp)
            j = 1
            while(j < len(reg_x_temp)):
                reg_x_temp[j] = reg_x_temp_two[j-1]
                j = j + 1
            reg_x_temp[0] = new

        if reg_y_temp[9] == majority:
            new_one = reg_x_temp[0] ^ reg_y_temp[20] ^ reg_y_temp[21]
            reg_y_temp_two = copy.deepcopy(reg_y_temp)
            k = 1
            while(k < len(reg_y_temp)):
                reg_y_temp[k] = reg_y_temp_two[k-1]
                k = k + 1
            reg_y_temp[0] = new_one

        if reg_z_temp[9] == majority:
            new_two = reg_x_temp[0] ^ reg_z_temp[7] ^ reg_z_temp[20] ^ reg_z_temp[21] ^ reg_z_temp[22]
            reg_z_temp_two = copy.deepcopy(reg_z_temp)
            m = 1
            while(m < len(reg_z_temp)):
                reg_z_temp[m] = reg_z_temp_two[m-1]
                m = m + 1
            reg_z_temp[0] = new_two

        keystream.insert(i, reg_x_temp[18] ^ reg_y_temp[21] ^ reg_z_temp[22])
        i = i + 1
    return keystream


def convert_binary_to_str(binary): #преобразует двоичный код в строку
    s = "".join(map(lambda x: chr(int(x,2)), binary))
    return str(s)

def encrypt_decrypt(plain): #принимает открытый текст, преобразует его в двоичный, получает ключевой поток после ввода длины двоичного текста и добавляет значения XOR ключевого потока и двоичного текста в строку
    s = []
    sh_kod=""
    binary = to_binary(plain)
    col_simv=len(binary*11)
    keystream = get_keystream(col_simv)
    i=0
    for kod_simv in binary:
        for ind_simv in range(len(kod_simv)):
            sh_kod += str(int(kod_simv[ind_simv]) ^ keystream[i])
            i += 1
        s.append(sh_kod)
        sh_kod=""
    shifr=convert_binary_to_str(s)
    return shifr

def user_input_key(): #ввести ключ
    the_key = str(input('Введите 64-битный ключ: '))
    if (len(the_key) == 64 and re.match("^([01])+", the_key)):
        return the_key
    else:
        while(len(the_key) != 64 and not re.match("^([01])+", the_key)):
            if (len(the_key) == 64 and re.match("^([01])+", the_key)):
                return the_key
            the_key = str(input('Введите 64-битный ключ: '))
    return the_key

def user_input_choice(): #выбрать операцию
    someIn = str(input('[0]: Выход\n[1]: Зашифровать\n[2]: Расшифровать\nНажмите 0, 1, или 2: '))
    if (someIn == '0' or someIn == '1' or someIn == '2'):
        return someIn
    else:
        while(someIn != '0' or someIn != '1' or someIn != '2'):
            if (someIn == '0' or someIn == '1' or someIn == '2'):
                return someIn
            someIn = str(input('[0]: Выход\n[1]: Зашифровать\n[2]: Расшифровать\nНажмите 0, 1, или 2: '))
    return someIn

def user_input_text(): #ввести открытый текст
    try:
        someIn = str(input('Введите открытый текст: '))
    except:
        someIn = str(input('Попробуйте снова: '))
    return someIn


def the_main(): #основная функция, которая обрабатывает входные данные пользователя 
    while(1):
        key = str(user_input_key())
        set_key(key)
        first_choice = user_input_choice()
        if(first_choice == '0'):
            print('Хорошего дня!!!')
            sys.exit(0)
        elif(first_choice == '1'):
            plaintext = str(user_input_text())
            print("Исходный текст = ",plaintext,end="\n")
            print("Зашифрованный текст = ",encrypt_decrypt(plaintext),end="\n\n\n")
        elif(first_choice == '2'):
            ciphertext = str(user_input_text())
            print("Зашифрованный текст = ",ciphertext,end="\n")
            print("Расшифрованный текст = ",encrypt_decrypt(ciphertext),end="\n\n\n")           

the_main()

##Пример 64-битного ключа: 0101001000011010110001110001100100101001000000110111111010110111
