#Квадрат Полибия

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
def crypting(temp_mas):
    print()
    print('Введите открытый текст: ')
    open_text = input('-> ')
    open_text = open_text.lower()
    open_text = predtext(open_text)
    crypt_text = []
    # Формирование массива из цифровых значений, соответствующих каждому символу исходного сообщения
    for i in open_text:
        try:
            index_x = 0
            for x in temp_mas:
                try:
                    index_sym = x.index(i)
                    crypt_sym = int(str(index_x + 1) + str(index_sym + 1))
                    crypt_text.append(crypt_sym)
                    index_x += 1
                    continue
                # Поиск ошибок
                except ValueError:
                    index_x += 1
                    continue
        except:
            print()
            print('Ошибка!')
            print()

    return print('Зашифрованный текст: ', crypt_text)


#Функция расшифрования
def decrypting(temp_mas):
    print()
    print('Введите зашифрованный текст: ')
    print('Вводите по две цифры через запятую: ')
    crypt_text = input('-> ')
    open_text = ''
    crypt_text = crypt_text.split(', ')
    # Поиск буквенного значения по номеру столбца и номеру строки
    for nums in crypt_text:
        x = nums[0]
        y = nums[1]
        x = int(x) - 1
        y = int(y) - 1
        open_text += temp_mas[x][y]
    open_text = obrtext(open_text)
    return print('Расшифрованный текст: ', open_text)


if __name__ == "__main__":

    print('Квадрат Полибия')
    # Квадрат Полибия
    mas_alph = [['а','б','в','г','д','е'],      #1
                ['ж','з','и','й','к','л'],     #2
                ['м','н','о','п','р','с'],     #3
                ['т','у','ф','х','ц','ч'],     #4
                ['ш','щ','ъ','ы','ь','э'],      #5
                ['ю','я','-','-','-','-']]      #6

    while True:
        print('\nКвадрат всегда 6х6')
        print('Введите "1", чтобы зашифровать текст')
        print('Введите "2", чтобы расшифровать текст')
        print()
        # Выбор шифрования\расшифровки
        choice = input('-> ')
        if choice == '1':
            print()
            crypting(mas_alph)
            print()
            continue
        elif choice == '2':
            print()
            decrypting(mas_alph)
            print()
