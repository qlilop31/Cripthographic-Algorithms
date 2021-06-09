class DH_Endpoint(object):

  def __init__(self, public_key1, public_key2, private_key):
    self.public_key1 = public_key1
    self.public_key2 = public_key2
    self.private_key = private_key
    self.full_key = None
# Генерация открытого ключа
  def generate_partial_key(self):
    partial_key = self.public_key1**self.private_key
    partial_key = partial_key % self.public_key2
    return partial_key

# Вычисление секретного ключа
  def generate_full_key(self, partial_key_r):
    full_key = partial_key_r**self.private_key
    full_key = full_key % self.public_key2
    self.full_key = full_key
    return full_key

g=2 # g
a=13 # a
p=17 # p
b=15 # b
Alice = DH_Endpoint(g, p, a)
Bob = DH_Endpoint(g, p, b)
#print("Открытый текст: ", message)
print("Параметры:")
print("g= ", g)
print("a= ", a)
print("p= ", p)
print("b= ", b)

# Алиса генерирует этот частичный ключ и отправим его Бобу по сети
A=Alice.generate_partial_key()
print("Открытый ключ Алисы: A = g**a mod p = 197 ^151 mod 199 =", A)

# Таким же образом Бобь посылает мне свои частичные ключи и передает их Алисе через сеть.
B=Bob.generate_partial_key()
print("Открытый ключ Боба: B = g**b mod p = 197 ^157 mod 199 =", B)

#Сравнение двух расчетов частичных ключей
# Это код получения секретного ключа s Алисы
a_full=Alice.generate_full_key(B)
print("Алиса вычисляет секретный ключ s: ", a_full)

#А вот код Боба, полученный с использованием открытого ключа Алисы:
b_full=Bob.generate_full_key(A)
print("Боб подсчитывает: ", b_full)
