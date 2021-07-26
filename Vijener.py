#Шифр Виженер
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
    sc = -1
    scc = -1
    sh = 0 # номер строки
    print('Введите ключ: ')
    k = input('-> ')
    for character in open_text: # Перебираем каждый символ открытого текста
        sc = -1
        for a in alph:
            sc += 1
            if k == a:
                sh = int(sc)
        sc = -1
        for j in alph:
            sc += 1 # перейти на другую строку
            if j == character: # Преобразуем строку в шифртекст
                crypt_text = crypt_text + str(alph[(int(sc) + sh) % 32]) # Находим символ (букву текста)
                k = str(alph[(int(sc) + sh) % 32]) # Находим символ ключа (сопоставляем их позиции)
    return print('Зашифрованный текст: ', crypt_text)

    
    

        
# Функция расшифрования
def decrypting():
    print('Введите зашифрованный текст: ')
    crypt_text = input('-> ')
    crypt_text = crypt_text.lower()
    print('Введите ключ: ')
    k = input('-> ')
    scl = 0
    sh = 0
    sc = -1
    open_text = ''
    for character in crypt_text: # Перебираем каждый зашифрованный символ
        sc = -1
        for a in alph:
            sc += 1
            if k == a:
                sh = int(sc)
        sc = -1
        for j in alph:
            sc += 1
            if j == character: # Обратная замена
                open_text = open_text + str(alph[(int(sc) - sh) % 32])
                k = str(alph[int(sc)])
    open_text = obrtext(open_text)
    return print('Расшифрованный текст: ', open_text)

if __name__ == "__main__":
    
    print('Шифр Вижнера')
# Алфавит в нижнем регистре
    alph = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
# Алфавит в верхнем регистре
    #alph2 = alph.upper()


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