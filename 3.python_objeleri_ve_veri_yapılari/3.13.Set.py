
"""
list
Sıralıdır, indekslenebilir.
Elemanlar tekrar edebilir.
Değiştirilebilir, dinamik yapılıdır.
append, insert, remove, pop gibi metotlar içerir.

tuple
Sıralıdır, indekslenebilir.
Elemanlar tekrar edebilir.
Değiştirilemez (immutable).
Haif ve hızlıdır. Sabit veri saklamak için kullanılır.

set
Sırasızdır, bu yüzden indekslenemez.
Elemanlar benzersiz olmalıdır.
Hızlı arama için uygundur (hash tabanlı).
add, remove, union, intersection gibi işlemler desteklenir.

dict
Anahtar-değer (key-value) yapısıdır.
Anahtarlar benzersiz ve hashlenebilir olmalıdır.
Sıralıdır (Python 3.7+), ancak indeksle değil anahtar ile erişilir.
Çok hızlı erişim sağlar.

str
Karakter dizileridir (Unicode).
Sıralı ve indekslenebilir.
Değiştirilemez (immutable); bir karakteri doğrudan değiştiremezsin, yeni bir string üretmelisin.
Metin işleme için çok sayıda yerleşik metod içerir (split, replace, find, vs).

Kullanım Senaryoları
Durum	                               En Uygun Veri Yapısı
Sıralı ve değiştirilebilir veri	         list
Sıralı ama sabit veri	                 tuple
Benzersiz öğeler	                     set
Anahtar-değer ilişkisi	                 dict
Metin verisi	                         str

"""
"""

Iterable Olma Şartı
Bir nesne eğer:
__iter__() metodunu tanımlamışsa
veya
__getitem__() metodunu tanımlamışsa (ve indeks 0’dan başlayarak sıralı olarak erişim sağlıyorsa) iterable sayılır.



Iterable Olanlar:
Bunlar for döngüsünde doğrudan kullanılabilir.
list
tuple
str
dict
set
range
enumerate, zip, map, filter

Iterable Olmayanlar:
Bunlar doğrudan for ile gezilemez:
int
float
bool
NoneType
complex
datetime.datetime (bazı özellikleri hariç)
object (kendi başına)

"""


fruits = {'orange', 'apple', 'banana'}

# setler indexlenemez
# print(fruits[0]) # TypeError: 'set' object is not subscriptable

# iterable dır
for fruit in fruits :
    print(fruit)
"""
orange
apple
banana
"""

# sıralayamıyoruz, sırasızdır

# eleman ekleme
fruits.add("cherry")
print(fruits) # {'banana', 'apple', 'cherry', 'orange'}

# birden fazla eleman ekleme
# update içine liste ile ekleyebiliriz
fruits.update(["mango", "grape"])
print(fruits)  # {'grape', 'cherry', 'orange', 'mango', 'apple', 'banana'}

fruits.update(["apple"])
print(fruits) # {'apple', 'grape', 'orange', 'mango', 'banana', 'cherry'}

myList = [1, 2, 5, 4, 4, 2, 1]
print(set(myList)) # {1, 2, 4, 5}

fruits.remove('mango')
print(fruits) # {'apple', 'grape', 'banana', 'cherry', 'orange'}

fruits.discard('apple')
print(fruits) # {'grape', 'orange', 'cherry', 'banana'}

fruits.pop()
print(fruits) # {'grape', 'cherry', 'orange'}

"""
list.pop(index=-1)
Listelerde pop(), varsayılan olarak son elemanı listeden çıkarır ve onu döndürür.
Eğer bir indeks verirseniz, o indeksteki elemanı çıkarır ve döndürür.
Sıralı yapılar olduğu için hangi elemanın çıkacağı belirlidir.

set.pop()
Setlerde pop() herhangi bir rastgele elemanı çıkarır ve döndürür.
Çünkü set sırasız bir yapıdır. Yani hangi elemanın çıkacağı önceden tahmin edilemez.
"""

fruits.clear()
print(fruits) # set()