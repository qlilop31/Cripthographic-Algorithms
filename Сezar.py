#Шифр Цезаря

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
def crypting(mas_temp, temp_len_mas):
    print()
    print('Введите открытый текст: ')
    open_text = input('-> ')
    open_text = open_text.lower()
    open_text = predtext(open_text)
    print()
    print('Введите ключ: ')
    key = int(input('-> '))
    crypt_text = ''
    # Замена символов сообщения на зашифрованные
    for character in open_text:
        try:
            i = mas_temp.index(character)
            crypt_text += mas_temp[i + key]
        # Проверка на ошибки
        except ValueError:
            print()
            print('Ошибка! -> ' + character)
            print()
        except IndexError:
            i = mas_temp.index(character)
            crypt_text += mas_temp[(i + key) - temp_len_mas]

    return print('Зашифрованный текст: ', crypt_text)
        
# Функция расшифрования
def decrypting(mas_temp):
    print()
    print('Введите зашифрованный текст: ')
    crypt_text = input('-> ')
    crypt_text = crypt_text.lower()
    print()
    print('Введите ключ: ')
    key = int(input('-> '))
    open_text = ''
    for character in crypt_text:
        try:
            i = mas_temp.index(character)
            open_text += mas_temp[i - key]
        # Проверка на ошибки
        except ValueError:
            print()
            print('Ошибка! -> ' + character)
            print()
    open_text = obrtext(open_text)
    return print('Расшифрованный текст: ', open_text)

if __name__ == "__main__":
    
    print('Шифр Цезаря')
# Алфавит из 32 букв русского алфавита и основных знаков препинания
    mas_alph = ['а','б','в','г','д','е',
                'ж','з','и','й','к','л',
                'м','н','о','п','р','с',
                'т','у','ф','х','ц','ч',
                'ш','щ','ъ','ы','ь','э',
                'ю','я']
# Вычисление длины алфавита
    len_mas = len(mas_alph)
    #print(len_mas)
    
#Выбор действия
    while True:
        print()
        print('Введите "1", чтобы зашифровать текст')
        print('Введите "2", чтобы расшифровать текст')
        print()
        # Выбор расшифрования\шифрования
        choice = input('-> ')
        if choice == '1':
            print()
            crypting(mas_alph, len_mas)
            print()
            continue
        elif choice == '2':
            print()
            decrypting(mas_alph)
            print()
            continue
