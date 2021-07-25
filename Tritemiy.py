#Шифр Тритемия

#Функция для формирования строки и удаления лишних символов
def predtext(open_text):
    open_text = open_text.lower()#Выравнивание строки - все прописные.
    open_text = open_text.replace('.', 'тчк') # Если в сообщении попадется точка, она заменится на тчк
    open_text = open_text.replace(',', 'зпт') # Если в сообщении попадется запятая, она заменится на зпт
    open_text = open_text.replace('-', 'тире') # Если в сообщении попадется тире, символ заменится на тире
    open_text = open_text.replace('!', 'вскзн') # Если в сообщении попадется !, символ заменится на вск\
    open_text = open_text.replace(':', 'двтчк') # Если в сообщении попадется :, символ заменится на двтчк
    open_text = open_text.replace('ё', 'е') # Если в сообщении попадется ё, буква заменится на е
    open_text = open_text.replace("'", '') # Если в сообщении попадется ' , символ удалим
    open_text = open_text.replace('""', '') # Если в сообщении попадется " , символ удалим
    open_text = open_text.replace("«", '') # Если в сообщении попадется « , символ удалим
    open_text = open_text.replace("»", '') # Если в сообщении попадется » , символ удалим
    open_text = open_text.replace('[', '') # Если в сообщении попадется [ , символ удалим
    open_text = open_text.replace(']', '') # Если в сообщении попадется ], символ удалим
    open_text = open_text.replace(' ', '') # Если в сообщении попадется пробел, символ заменим на пробел
    open_text = open_text.replace('\\n', 'слэш') # Если в сообщение разделяется, то и это заменим на слэш
    open_text = open_text.replace('слэшзпт', 'слэш')
    return open_text

#Функция для формирования обычной строки со всеми символами
def obrtext(open_text):
    open_text = open_text.lower()
    open_text = open_text.replace('тчк','.' ) 
    open_text = open_text.replace('зпт',',' ) 
    open_text = open_text.replace('тире','-' )
    open_text = open_text.replace('вскзн','!' ) 
    open_text = open_text.replace('двтчк', ':')
    #open_text = open_text.replace('прбл',' ' )
    open_text = open_text.replace('слэш','\n' )
    return open_text


# Функция шифрования
def crypting():
    print()
    print('Введите открытый текст: ')
    open_text = input('-> ')
    open_text = predtext(open_text)
    open_text = open_text.lower()
    crypt_text = ''
    k = 0
    for character in open_text: #блок шифрования
        if character.isupper():
        # L = (m + k) mod N для больших букв
            crypt_text += alph2[(alph2.find(character) + k) % len(alph2)]
        elif character.islower():
        # L = (m + k) mod N для маленьких букв
            crypt_text += alph[(alph.find(character) + k) % len(alph)]
        else:
            crypt_text += character
        k += 1
    return print('Зашифрованный текст: ', crypt_text)
        
# Функция расшифрования
def decrypting():
    print('Введите зашифрованный текст: ')
    crypt_text = input('-> ')
    crypt_text = crypt_text.lower()
    k = 0
    open_text = ''
    # Блок расшифровки. Всё по аналогии с шифрованием
    for character in crypt_text:#блок расшифрования
        if character.isupper():
        # L = (m - k) mod N для больших букв
            open_text += alph2[(alph2.find(character) - k) % len(alph2)]
        elif character.islower():
        # L = (m - k) mod N для маленьких букв
            open_text += alph[(alph.find(character) - k) % len(alph)]
        else:
            open_text += character
        k += 1
    open_text=obrtext(open_text)
    return print('Расшифрованный текст: ', open_text)

if __name__ == "__main__":
    
    print('Шифр Тритемия')
# Алфавит в нижнем регистре
    alph = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
# Алфавит в верхнем регистре
    alph2 = alph.upper()


    while True:
        print()
        print('Введите "1", чтобы зашифровать текст')
        print('Введите "2", чтобы расшифровать текст')
        print()
        # Выбор расшифрования\шифрования
        choice = input('-> ')
        if choice == '1':
            print()
            crypting()
            print()
            continue
        elif choice == '2':
            print()
            decrypting()
            print()
            continue

pause()
