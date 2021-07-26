from functools import partial
from codecs import getdecoder
from codecs import getencoder
from sys import version_info
# Функция для формирования строки и удаления лишних символов
def predtext(s):
    s = s.lower() # Выравнивание строки - все прописные.
    s = s.replace('.', 'тчк') # Если в сообщении попадется точка, 
                              #она заменется на тчк
    s = s.replace(',', 'зпт') # Если в сообщении попадется запятая, 
                              #она заменется на зпт
    s = s.replace('-', 'тире') # Если в сообщении попадется тире, 
                               # символ заменется на тире
    s = s.replace("'", '') # Если в сообщении попадется ' при 
                            #выгрузке из файла, символ удалим
    s = s.replace(";", 'тчкзпт') # Если в сообщении попадется ; при 
                            #выгрузке из файла, символ заменим
    s = s.replace('[', '') # Если в сообщении попадется [ при 
                            #выгрузке из файла, символ удалим
    s = s.replace(']', '') # Если в сообщении попадется ] при 
                            #выгрузке из файла, символ удалим
    s = s.replace(' ', '') # Если в сообщении попадется пробел при 
                            #выгрузке из файла, символ удалим
    s = s.replace('щ', 'шч')   # Так как алфавит русский намного больше, 
                               # чем английский, то недостоющие
    s = s.replace('ь', 'мгк') # символы заменим на обозначения.
    s = s.replace('ъ', 'тврз')
    s = s.replace('э', 'йе')
    s = s.replace('ю', 'йу')
    s = s.replace('я', 'йа')
    s = s.replace('ы', 'йи')
    return s 
# Функция для формирования обычной строки со всеми символами
def obrtext(s):
    s = s.lower()
    s = s.replace('тчк','.' ) 
    s = s.replace('зпт',',' ) 
    s = s.replace('тире','-' )
    s = s.replace('шч', 'щ')
    s = s.replace('мгк', 'ь')
    s = s.replace('тврз', 'ъ')
    s = s.replace('йе', 'э')
    s = s.replace('йу','ю')
    s = s.replace('йа', 'я')
    s = s.replace('йи', 'ы')
    return s
 
 
KEYSIZE = 32  # размер ключа
BLOCKSIZE = 8 # размер блока
C1 = 0x01010104
C2 = 0x01010101
 
 
xrange = range if version_info[0] == 3 else xrange  # pylint: disable=redefined-builtin
 
_hexdecoder = getdecoder("hex")
_hexencoder = getencoder("hex")
 
def hexdec(data):
    """Расшифровать шестнадцатеричный
    """
    return _hexdecoder(data)[0]
 
def strxor(a, b):
    """ XOR двух строк
 
    Эта функция будет обрабатывать только самую короткую длину обеих строк,
     игнорируя оставшийся.
    """
    mlen = min(len(a), len(b))
    a, b, xor = bytearray(a), bytearray(b), bytearray(mlen)
    for i in range(mlen):
        xor[i] = a[i] ^ b[i]
    return bytes(xor)
 
 
 
""" Последовательность применения K_i S-блока  для шифрования и дешифрования"""
SEQ_ENCRYPT = (
    0, 1, 2, 3, 4, 5, 6, 7,
    0, 1, 2, 3, 4, 5, 6, 7,
    0, 1, 2, 3, 4, 5, 6, 7,
    7, 6, 5, 4, 3, 2, 1, 0,
)
SEQ_DECRYPT = (
    0, 1, 2, 3, 4, 5, 6, 7,
    7, 6, 5, 4, 3, 2, 1, 0,
    7, 6, 5, 4, 3, 2, 1, 0,
    7, 6, 5, 4, 3, 2, 1, 0,
)
 
# S-блок параметры
DEFAULT_SBOX = "id-Gost28147-89-CryptoPro-A-ParamSet"
SBOXES = {
    "id-Gost28147-89-TestParamSet": (
        (4, 2, 15, 5, 9, 1, 0, 8, 14, 3, 11, 12, 13, 7, 10, 6),
        (12, 9, 15, 14, 8, 1, 3, 10, 2, 7, 4, 13, 6, 0, 11, 5),
        (13, 8, 14, 12, 7, 3, 9, 10, 1, 5, 2, 4, 6, 15, 0, 11),
        (14, 9, 11, 2, 5, 15, 7, 1, 0, 13, 12, 6, 10, 4, 3, 8),
        (3, 14, 5, 9, 6, 8, 0, 13, 10, 11, 7, 12, 2, 1, 15, 4),
        (8, 15, 6, 11, 1, 9, 12, 5, 13, 3, 7, 10, 0, 14, 2, 4),
        (9, 11, 12, 0, 3, 6, 7, 5, 4, 8, 14, 15, 1, 10, 2, 13),
        (12, 6, 5, 2, 11, 0, 9, 13, 3, 14, 7, 10, 15, 4, 1, 8),
    ),
    "id-Gost28147-89-CryptoPro-A-ParamSet": (
        (9, 6, 3, 2, 8, 11, 1, 7, 10, 4, 14, 15, 12, 0, 13, 5),
        (3, 7, 14, 9, 8, 10, 15, 0, 5, 2, 6, 12, 11, 4, 13, 1),
        (14, 4, 6, 2, 11, 3, 13, 8, 12, 15, 5, 10, 0, 7, 1, 9),
        (14, 7, 10, 12, 13, 1, 3, 9, 0, 2, 11, 4, 15, 8, 5, 6),
        (11, 5, 1, 9, 8, 13, 15, 0, 14, 4, 2, 3, 12, 7, 10, 6),
        (3, 10, 13, 12, 1, 2, 0, 11, 7, 5, 9, 4, 8, 15, 14, 6),
        (1, 13, 2, 9, 7, 10, 6, 0, 8, 12, 4, 5, 15, 3, 11, 14),
        (11, 10, 15, 5, 0, 12, 14, 8, 6, 2, 3, 9, 1, 7, 13, 4),
    ),
    "id-Gost28147-89-CryptoPro-B-ParamSet": (
        (8, 4, 11, 1, 3, 5, 0, 9, 2, 14, 10, 12, 13, 6, 7, 15),
        (0, 1, 2, 10, 4, 13, 5, 12, 9, 7, 3, 15, 11, 8, 6, 14),
        (14, 12, 0, 10, 9, 2, 13, 11, 7, 5, 8, 15, 3, 6, 1, 4),
        (7, 5, 0, 13, 11, 6, 1, 2, 3, 10, 12, 15, 4, 14, 9, 8),
        (2, 7, 12, 15, 9, 5, 10, 11, 1, 4, 0, 13, 6, 8, 14, 3),
        (8, 3, 2, 6, 4, 13, 14, 11, 12, 1, 7, 15, 10, 0, 9, 5),
        (5, 2, 10, 11, 9, 1, 12, 3, 7, 4, 13, 0, 6, 15, 8, 14),
        (0, 4, 11, 14, 8, 3, 7, 1, 10, 2, 9, 6, 15, 13, 5, 12),
    ),
    "id-Gost28147-89-CryptoPro-C-ParamSet": (
        (1, 11, 12, 2, 9, 13, 0, 15, 4, 5, 8, 14, 10, 7, 6, 3),
        (0, 1, 7, 13, 11, 4, 5, 2, 8, 14, 15, 12, 9, 10, 6, 3),
        (8, 2, 5, 0, 4, 9, 15, 10, 3, 7, 12, 13, 6, 14, 1, 11),
        (3, 6, 0, 1, 5, 13, 10, 8, 11, 2, 9, 7, 14, 15, 12, 4),
        (8, 13, 11, 0, 4, 5, 1, 2, 9, 3, 12, 14, 6, 15, 10, 7),
        (12, 9, 11, 1, 8, 14, 2, 4, 7, 3, 6, 5, 10, 0, 15, 13),
        (10, 9, 6, 8, 13, 14, 2, 0, 15, 3, 5, 11, 4, 1, 12, 7),
        (7, 4, 0, 5, 10, 2, 15, 14, 12, 6, 1, 11, 13, 9, 3, 8),
    ),
    "id-Gost28147-89-CryptoPro-D-ParamSet": (
        (15, 12, 2, 10, 6, 4, 5, 0, 7, 9, 14, 13, 1, 11, 8, 3),
        (11, 6, 3, 4, 12, 15, 14, 2, 7, 13, 8, 0, 5, 10, 9, 1),
        (1, 12, 11, 0, 15, 14, 6, 5, 10, 13, 4, 8, 9, 3, 7, 2),
        (1, 5, 14, 12, 10, 7, 0, 13, 6, 2, 11, 4, 9, 3, 15, 8),
        (0, 12, 8, 9, 13, 2, 10, 11, 7, 3, 6, 5, 4, 14, 15, 1),
        (8, 0, 15, 3, 2, 5, 14, 11, 1, 10, 4, 7, 12, 9, 13, 6),
        (3, 0, 6, 15, 1, 14, 9, 2, 13, 8, 12, 4, 11, 10, 5, 7),
        (1, 10, 6, 8, 15, 11, 0, 4, 12, 3, 5, 9, 7, 13, 2, 14),
    ),
    "id-tc26-gost-28147-param-Z": (
        (12, 4, 6, 2, 10, 5, 11, 9, 14, 8, 13, 7, 0, 3, 15, 1),
        (6, 8, 2, 3, 9, 10, 5, 12, 1, 14, 4, 7, 11, 13, 0, 15),
        (11, 3, 5, 8, 2, 15, 10, 13, 14, 1, 7, 4, 12, 9, 6, 0),
        (12, 8, 2, 1, 13, 4, 15, 6, 7, 0, 10, 5, 3, 14, 9, 11),
        (7, 15, 5, 10, 8, 1, 6, 13, 0, 9, 3, 14, 11, 4, 2, 12),
        (5, 13, 15, 6, 9, 2, 12, 10, 11, 7, 8, 1, 4, 3, 14, 0),
        (8, 14, 2, 5, 6, 9, 1, 12, 15, 4, 11, 0, 13, 10, 3, 7),
        (1, 7, 14, 13, 0, 5, 8, 3, 4, 15, 10, 6, 9, 12, 11, 2),
    ),
    "id-GostR3411-94-TestParamSet": (
        (4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3),
        (14, 11, 4, 12, 6, 13, 15, 10, 2, 3, 8, 1, 0, 7, 5, 9),
        (5, 8, 1, 13, 10, 3, 4, 2, 14, 15, 12, 7, 6, 0, 9, 11),
        (7, 13, 10, 1, 0, 8, 9, 15, 14, 4, 6, 12, 11, 2, 5, 3),
        (6, 12, 7, 1, 5, 15, 13, 8, 4, 10, 9, 14, 0, 3, 11, 2),
        (4, 11, 10, 0, 7, 2, 1, 13, 3, 6, 8, 5, 9, 12, 15, 14),
        (13, 11, 4, 1, 3, 15, 5, 9, 0, 10, 14, 7, 6, 8, 2, 12),
        (1, 15, 13, 0, 5, 7, 10, 4, 9, 2, 3, 14, 6, 11, 8, 12),
    ),
    "id-GostR3411-94-CryptoProParamSet": (
        (10, 4, 5, 6, 8, 1, 3, 7, 13, 12, 14, 0, 9, 2, 11, 15),
        (5, 15, 4, 0, 2, 13, 11, 9, 1, 7, 6, 3, 12, 14, 10, 8),
        (7, 15, 12, 14, 9, 4, 1, 0, 3, 11, 5, 2, 6, 10, 8, 13),
        (4, 10, 7, 12, 0, 15, 2, 8, 14, 1, 6, 5, 13, 11, 9, 3),
        (7, 6, 4, 11, 9, 12, 2, 10, 1, 8, 0, 14, 15, 13, 3, 5),
        (7, 6, 2, 4, 13, 9, 15, 0, 10, 1, 5, 11, 8, 14, 12, 3),
        (13, 14, 4, 1, 7, 0, 5, 10, 3, 12, 8, 15, 6, 2, 9, 11),
        (1, 3, 10, 9, 5, 11, 4, 15, 8, 6, 7, 14, 13, 0, 2, 12),
    ),
    "EACParamSet": (
        (11, 4, 8, 10, 9, 7, 0, 3, 1, 6, 2, 15, 14, 5, 12, 13),
        (1, 7, 14, 9, 11, 3, 15, 12, 0, 5, 4, 6, 13, 10, 8, 2),
        (7, 3, 1, 9, 2, 4, 13, 15, 8, 10, 12, 6, 5, 0, 11, 14),
        (10, 5, 15, 7, 14, 11, 3, 9, 2, 8, 1, 12, 0, 4, 6, 13),
        (0, 14, 6, 11, 9, 3, 8, 4, 12, 15, 10, 5, 13, 7, 1, 2),
        (9, 2, 11, 12, 0, 4, 5, 6, 3, 15, 13, 8, 1, 7, 14, 10),
        (4, 0, 14, 1, 5, 11, 8, 3, 12, 2, 9, 7, 6, 10, 13, 15),
        (7, 14, 12, 13, 9, 4, 8, 15, 10, 2, 6, 0, 3, 11, 5, 1),
    ),
}
SBOXES["AppliedCryptography"] = SBOXES["id-GostR3411-94-TestParamSet"]
 
 
def _K(s, _in):
    """ замена S-блоков
 
    :s параметр: S-блок
    :_in параметр : 32-bit слово
    :returns: замена 32-bit слово
    """
    return (
        (s[0][(_in >> 0) & 0x0F] << 0) +
        (s[1][(_in >> 4) & 0x0F] << 4) +
        (s[2][(_in >> 8) & 0x0F] << 8) +
        (s[3][(_in >> 12) & 0x0F] << 12) +
        (s[4][(_in >> 16) & 0x0F] << 16) +
        (s[5][(_in >> 20) & 0x0F] << 20) +
        (s[6][(_in >> 24) & 0x0F] << 24) +
        (s[7][(_in >> 28) & 0x0F] << 28)
    )
 
 
def block2ns(data):
    """ Конвертировать блок в  N1 и N2 integers
    """
    data = bytearray(data)
    return (
        data[0] | data[1] << 8 | data[2] << 16 | data[3] << 24,
        data[4] | data[5] << 8 | data[6] << 16 | data[7] << 24,
    )
 
 
def ns2block(ns):
    """ Преобразование N1 и N2 integers в 8-byte блок
    """
    n1, n2 = ns
    return bytes(bytearray((
        (n2 >> 0) & 255, (n2 >> 8) & 255, (n2 >> 16) & 255, (n2 >> 24) & 255,
        (n1 >> 0) & 255, (n1 >> 8) & 255, (n1 >> 16) & 255, (n1 >> 24) & 255,
    )))
 
 
def addmod(x, y, mod=2 ** 32):
    """ Сложение двух чисел по модулю 32
    """
    r = x + y
    return r if r < mod else r - mod
 
 
def _shift11(x):
    """ 11-битный циклический сдвиг
    """
    return ((x << 11) & (2 ** 32 - 1)) | ((x >> (32 - 11)) & (2 ** 32 - 1))
 
 
def validate_key(key):
    if len(key) != KEYSIZE:
        raise ValueError("Неверный размер ключа")
 
 
def validate_iv(iv):
    if len(iv) != BLOCKSIZE:
        raise ValueError("Неверный размер ключа инициализации")
 
 
def validate_sbox(sbox):
    if sbox not in SBOXES:
        raise ValueError("Неизвестный sbox")
 
 
def xcrypt(seq, sbox, key, ns):
    """ Полный раунд работы одного блока
 
    :param seq: последовательность применения K_i S-box  (либо зашифровать либо расшифровать)
    :param sbox:параметры  S-блока
    :type sbox: str
    :param bytes key: 256-bit ключ шифрования
    :param ns: N1 и N2 integers
    :type ns: (int, int)
    :returns: новые N1 и N2
    :rtype: (int, int)
    """
    s = SBOXES[sbox]
    w = bytearray(key)
    x = [
        w[0 + i * 4] |
        w[1 + i * 4] << 8 |
        w[2 + i * 4] << 16 |
        w[3 + i * 4] << 24 for i in range(8)
    ]
    n1, n2 = ns
    for i in seq:
        n1, n2 = _shift11(_K(s, addmod(n1, x[i]))) ^ n2, n1
    return n1, n2
 
 
def encrypt(sbox, key, ns):
    """ Зашифровать один блок
    """
    return xcrypt(SEQ_ENCRYPT, sbox, key, ns)
 
 
def decrypt(sbox, key, ns):
    """ Расшифровать один блок
    """
    return xcrypt(SEQ_DECRYPT, sbox, key, ns)
 
 
def ecb(key, data, action, sbox=DEFAULT_SBOX):
    """ Режим простой замены
 
    :param bytes key: ключ зашифрования
    :param data: исходный текст
    :type data: bytes, кратный BLOCKSIZE
    :param func action: "encrypt"/"decrypt"
    :param sbox: S-блок
    :type sbox: str, SBOXES'es key
    :returns: шифртекст
    :rtype: bytes
    """
    validate_key(key)
    validate_sbox(sbox)
    if not data or len(data) % BLOCKSIZE != 0:
        raise ValueError("Данные не выровнены по размеру блока")
    result = []
    for i in range(0, len(data), BLOCKSIZE):
        result.append(ns2block(action(
            sbox, key, block2ns(data[i:i + BLOCKSIZE])
        )))
    return b"".join(result)
 
 
ecb_encrypt = partial(ecb, action=encrypt)
ecb_decrypt = partial(ecb, action=decrypt)
 
def pad2(data, blocksize):
    """Метод заполнения 2 (ISO/IEC 7816-4)
 
   Добавить один бит, а затем заполняет нулями
    """
    return data + b"\x80" + b"\x00" * pad_size(len(data) + 1, blocksize)
 
def pad_size(data_size, blocksize):
    """Рассчитать необходимый размер pad для полного размера блока
    """
    if data_size < blocksize:
        return blocksize - data_size
    if data_size % blocksize == 0:
        return 0
    return blocksize - data_size % blocksize
 
def unpad2(data, blocksize):
    """Unpad метод 2
    """
    last_block = bytearray(data[-blocksize:])
    pad_index = last_block.rfind(b"\x80")
    if pad_index == -1:
        raise ValueError("Недопустимо")
    for c in last_block[pad_index + 1:]:
        if c != 0:
            raise ValueError("Недопустимо")
    return data[:-(blocksize - pad_index)]
 
 
 
 
def ctr(key, data, iv=8 * b"\x00", sbox=DEFAULT_SBOX):
    """ Режим гаммирования 
 
    :param bytes key: ключ
    :param bytes data: текст
    :param iv: вектор инициализации
    :type iv: bytes, BLOCKSIZE length
    :param sbox: S-блок
    :type sbox: str, SBOXES'es key
    :returns: шифротекст
    :rtype: bytes
Для расшифровки используется та же функция.
 
    """
    print(iv)
    validate_key(key)
    validate_iv(iv)
    validate_sbox(sbox)
    if not data:
        raise ValueError("Нет данных")
    n2, n1 = encrypt(sbox, key, block2ns(iv))
    gamma = []
    for _ in range(0, len(data) + pad_size(len(data), BLOCKSIZE), BLOCKSIZE):
        n1 = addmod(n1, C2, 2 ** 32)
        n2 = addmod(n2, C1, 2 ** 32 - 1)
        gamma.append(ns2block(encrypt(sbox, key, (n1, n2))))
    return strxor(b"".join(gamma), data)
 
 
MESH_CONST = hexdec("6900722264C904238D3ADB9646E92AC418FEAC9400ED0712C086DCC2EF4CA92B")
MESH_MAX_DATA = 1024
 
 
def meshing(key, iv, sbox=DEFAULT_SBOX):
    """:rfc:`4357` зацепление ключей
    """
    key = ecb_decrypt(key, MESH_CONST, sbox=sbox)
    iv = ecb_encrypt(key, iv, sbox=sbox)
    return key, iv
 
def cfb_encrypt(key, data, iv=8 * b"\x00", sbox=DEFAULT_SBOX, mesh=False):
    """ Режим обратной связи по шифротексту зашифрование
 
    :param bytes key: ключ
    :param bytes data: текст
    :param iv: вектор инициализации
    :type iv: bytes, BLOCKSIZE length
    :param sbox: S-блок
    :type sbox: str, SBOXES'es key
    :param bool mesh: зацепление ключей
    :returns: шифртекст
    :rtype: bytes
    """
    validate_key(key)
    validate_iv(iv)
    validate_sbox(sbox)
    if not data:
        raise ValueError("Данные не были введены")
    ciphertext = [iv]
    for i in range(0, len(data) + pad_size(len(data), BLOCKSIZE), BLOCKSIZE):
        if mesh and i >= MESH_MAX_DATA and i % MESH_MAX_DATA == 0:
            key, iv = meshing(key, ciphertext[-1], sbox=sbox)
            ciphertext.append(strxor(
                data[i:i + BLOCKSIZE],
                ns2block(encrypt(sbox, key, block2ns(iv))),
            ))
            continue
        ciphertext.append(strxor(
            data[i:i + BLOCKSIZE],
            ns2block(encrypt(sbox, key, block2ns(ciphertext[-1]))),
        ))
    return b"".join(ciphertext[1:])
 
 
def cfb_decrypt(key, data, iv=8 * b"\x00", sbox=DEFAULT_SBOX, mesh=False):
    """ Режим обратной связи по шифротексту расшифрование
 
    :param bytes key: ключ
    :param bytes data: текст
    :param iv: вектор инициализации
    :type iv: bytes, BLOCKSIZE length
    :param sbox: S-блок
    :type sbox: str, SBOXES'es key
    :param bool mesh:зацепление ключей
    :returns: текст
    :rtype: bytes
    """
    validate_key(key)
    validate_iv(iv)
    validate_sbox(sbox)
    if not data:
        raise ValueError("Данные не представлены")
    plaintext = []
    data = iv + data
    for i in range(BLOCKSIZE, len(data) + pad_size(len(data), BLOCKSIZE), BLOCKSIZE):
        if (
                mesh and
                (i - BLOCKSIZE) >= MESH_MAX_DATA and
                (i - BLOCKSIZE) % MESH_MAX_DATA == 0
        ):
            key, iv = meshing(key, data[i - BLOCKSIZE:i], sbox=sbox)
            plaintext.append(strxor(
                data[i:i + BLOCKSIZE],
                ns2block(encrypt(sbox, key, block2ns(iv))),
            ))
            continue
        plaintext.append(strxor(
            data[i:i + BLOCKSIZE],
            ns2block(encrypt(sbox, key, block2ns(data[i - BLOCKSIZE:i]))),
        ))
    return b"".join(plaintext)
 
 
 
#Работа с файлами
# !! Выбрать файл, с которым будет работать программа
vibor = input("нажмите 1 для работы с пословицей; 2 - с текстом: ") 
if vibor == '1':
    file = open("my_proverb.txt", "r")#открыть файл для чтения
else:
    file = open("my_text.txt", "r")#открыть файл для чтения на 1000 символов
data = file.readlines() #читать все строки
file.close()
text_fail = str(data)
print("Ваша строка:  ", text_fail)
text_fail = predtext(str(data))
# Выводим значения на экран для собственной проверки
print("Преобразованная строка: \n", text_fail)
 
text = text_fail.encode('cp1251')
print("Закодированная строка: \n", text)
 
# Запись закодированного сообщения
file = open("zakod.txt", "w")
file.writelines('Ваше закодированное сообщение: \n')
file.writelines (str(text))
file.seek(0)
file.close()
 
key = hexdec(b"75713134B60FEC45A607BB83AA3746AF4FF99DA6D1B53B5B1B402A1BAA030D1B")
sbox = "id-GostR3411-94-TestParamSet"
i=0
while (i!=3):
    print("Данная программа реализована с выбором режима работы.")
    print("1.Режим простой замены (ECB)")
    print("2.Режим гаммирования (CTR)")
    print("3.Режим обратной связи по шифротексту(CFB) \n ")
    vibor = int(input("Выберите цифру: "))
    if vibor == 1:
        er =ecb_encrypt(
                    key,
                    text,
                    sbox=sbox
                )
        ek=ecb_decrypt(
                    key,
                    er,
                    #iv=hexdec(b"0102030405060708"),
                    sbox=sbox,
                )
        new_ek = ek.decode('cp1251')
        itog_ek = obrtext(new_ek)
        print("Зашифрованное сообщение путем простой замены:\n ", er)
        print("Расшифрованное сообщение путем простой замены:\n ", ek)
        print("Раскодированное сообщение путем простой замены:\n ", itog_ek)
        print("\n")
 
    if vibor == 2:
        er =ctr(
                key,
                text,
                iv=hexdec(b"0102030405060708"),
                sbox=sbox
                )
        ek=ctr(
                key,
                er,
                iv=hexdec(b"0102030405060708"),
                sbox=sbox,
                )
        new_ek = ek.decode('cp1251')
        itog_ek = obrtext(new_ek)
        print("Зашифрованное сообщение путем гаммирования:\n ", er)
        print("Расшифрованное сообщение путем гаммирования:\n ", ek)
        print("Раскодированное сообщение путем гаммирования:\n ", itog_ek)
        print("\n")
    if vibor == 3:
        er=cfb_encrypt(
                        key,
                        text,
                        iv=hexdec(b"0102030405060708"),
                        sbox=sbox,
                    )
        ek=cfb_decrypt(
                    key,
                    er,
                    iv=hexdec(b"0102030405060708"),
                    sbox=sbox,
                )
        new_ek = ek.decode('cp1251')
        itog_ek = obrtext(new_ek)
        print("Зашифрованное сообщение через режим обратной связи по шифротексту:\n ", er)
        print("Расшифрованное сообщение через режим обратной связи по шифротексту:\n ", ek)
        print("Раскодированное сообщение через режим обратной связи по шифротексту:\n ", itog_ek)
        print("\n")
    i+=1
 
# Запись зашифрованного сообщения
file = open("shifrtext.txt", "w")
file.writelines('Ваше зашифрованное сообщение: \n '+str(er))
file.seek(0)
file.close()
 
new_ek = ek.decode('cp1251')
itog_ek = obrtext(new_ek)
print(itog_ek)
 
# Запись расшифрованного сообщения
file = open("rasshifr.txt", "w")
str1 = 'Ваше расшифрованное сообщение: \n '+str(ek)
file.writelines(str1)
file.seek(0)
file.close()
