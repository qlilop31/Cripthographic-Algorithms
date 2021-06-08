# Атбаш
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
    open_text = open_text.replace(' ', 'прбл') # Если в сообщении попадется пробел, символ заменим на пробел
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
    open_text = open_text.replace('прбл',' ' )
    open_text = open_text.replace('слэш','\n' )
    return open_text

# Функция шифрования
def crypting(temp_mas, temp_char_mas):
    print()
    print('Введите открытый текст: ')
    open_text = input('Вы -> ')
    open_text = open_text.lower()
    #print(open_text)
    open_text = predtext(open_text)
    #print(open_text)
    crypt_text = ''
    for character in open_text:
        try:
            i = temp_mas.index(character)
            crypt_text += temp_mas[-i]
            # print('crypt = ' + crypt_text + ' char = ' + character)
        # Проверка на ошибки
        except ValueError:
            try:
                i = temp_char_mas.index(character)
                crypt_text += temp_char_mas[-i]
                # print('crypt = ' + crypt_text + ' char = ' + character)
            except ValueError:
                print()
                print('Ошибка! -> ' + character)
                print()

    return print('Зашифрованный текст: ', crypt_text)


# Функция расшифрования
def decrypting(temp_mas, temp_char_mas):
    print()
    print('Введите зашифрованный текст: ')
    crypt_text = input('Вы -> ')
    crypt_text = crypt_text.lower()
    open_text = ''
    for character in crypt_text:
        try:
            i = temp_mas.index(character)
            open_text += temp_mas[-i]
        # Проверка на ошибки
        except ValueError:
            try:
                i = temp_char_mas.index(character)
                open_text += temp_char_mas[-i]
            except ValueError:
                print()
                print('Ошибка! -> ' + character)
                print()
    #print(open_text)
    open_text = obrtext(open_text)
    #print(open_text)
    return print('Расшифрованный текст: ', open_text)


if __name__ == "__main__":

    print('Шифр Атбаш')

    mas_alph = ['', 'а', 'б', 'в', 'г', 'д', 'е',
                'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н',
                'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы',
                'ь', 'э', 'ю', 'я']

    mas_char = ['', ' ', ',', '.', '!', '?']

    while True:
        print()
        print('Введите "1", чтобы зашифровать текст')
        print('Введите "2", чтобы расшифровать текст')
        print()
        # Выбор шифрования или расшифровки
        choice = input('Вы -> ')
        if choice == '1':
            print()
            crypting(mas_alph, mas_char)
            print()
            continue
        elif choice == '2':
            print()
            decrypting(mas_alph, mas_char)
            print()
            continue

