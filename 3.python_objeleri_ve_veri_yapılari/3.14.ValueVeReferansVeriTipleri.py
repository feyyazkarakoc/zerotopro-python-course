
#  value types => int, float, complex, str, Tuple, Boolean (bool), Frozenset

x = 5
y = 25

x = y # x ve y farklı alanlarda tanımlandı

y = 10

print(x , y) # 25 10 # y'de yaptığımız değişiklik x'i etkilemedi

# referance types => list, class

a = ["apple", "banana"]
b = ["apple", "banana"] # a ve b adres tutuyor, adreslerde de listenin içindekiler tutulur 

print("a id : " ,id(a), "b id : ", id(b)) # a id :  2180528181184 b id :  2180532010432

a = b # a ve b aynı alanlarda tanımlandı, aynı adresi gösteriyor
print("a id : " ,id(a), "b id : ", id(b)) # a id :  2180532010432 b id :  2180532010432

b[0] = "graphe"

print(a, b) # ['graphe', 'banana'] ['graphe', 'banana']
print("a id : " ,id(a), "b id : ", id(b)) # a id :  2180532010432 b id :  2180532010432

# a'da bir değişiklik yapmadık, b'de yaptığımız değişiklik a'yı da etkiledi. value type'larda böyle bir değişiklik olmadı

"""

a = ["apple", "banana"]
b = ["apple", "banana"]
Bu durumda a ve b ayrı listelerdir.

Her biri farklı bir bellekteki listeyi işaret eder.
Bu yüzden id(a) != id(b).

Referansların Eşitlenmesi:
a = b
Artık a ve b aynı listeyi işaret eder.
a sadece b ile aynı adresi göstermeye başlar.
Yani a artık b'nin referansını taşır, kendi önceki listesini bırakır.
id(a) == id(b) olur.

Listede Değişiklik:
b[0] = "graphe"
print(a)  # ['graphe', 'banana']
a ve b aynı listeyi gösterdiği için b üzerinden yapılan değişiklik a'yı da etkiler.
Daha Doğru Şekilde İfade Edilmesi Gerekenler:
"a ve b aynı alanlarda tanımlandı"--->>> "a, b ile aynı listeyi göstermeye başladı"
"adreslerde de listenin içindekiler tutulur"--->>"Değişkenler adres (referans) tutar, içerik o adresin gösterdiği yerde saklanır"

Özetle:
a ve b referans (adres) tutar.
a = b dediğinizde a artık b ile aynı adresi tutar.
O liste üzerinde yapılan her değişiklik, onu gösteren tüm referansları (a ve b) etkiler.
Bu durum, değer tiplerinden (int, float, bool, vs) farklıdır. Değer tiplerinde değişiklikler kopya üzerinde olur.
"""

# *********************************************************************************************************************


# Referans demek adres demek
# Fonksiyonların ve değişkenlerin birer adresi var

x = 5
print(id(x)) # 140712689693608 bellek adresi

print(id(5)) # 140712689693608

def yaz() :
    return (id(yaz))

print(yaz()) # 1654174078976

print(id(yaz)) # 1654174078976 bellek adresi

# del ile kullanırsak bellekten atmış oluruz, artık bellekte yaşamıyorlar

del x
del yaz

# print(id(x)) # NameError: name 'x' is not defined
# print(id(yaz)) # NameError: name 'yaz' is not defined

def benidegistir(l) :
    l.append(["1", "2" , 3])
    print("Fonksiyon içi : ",l)
    print(id(l))

my_list = ["Deneme", 34, 4.54]

print("my_list : ", my_list) # my_list :  ['Deneme', 34, 4.54]
benidegistir(my_list) # Fonksiyon içi :  ['Deneme', 34, 4.54, ['1', '2', 3]]
print("my_list fonksiyondan sonra : ", my_list) # my_list fonksiyondan sonra :  ['Deneme', 34, 4.54, ['1', '2', 3]]

print(id(my_list)) # 2900326584256
benidegistir(my_list) # 2900326584256
# Aynı bellek adresine sahipler, çünkü fonksiyona referans (adres) gönderilir

my_list2 = [1 , 2, 3]
print(my_list2, id(my_list2)) # [1, 2, 3] 2109026499008

def benidegistir2(l) :
    l = [4  ,5, 6]   # eşittir yaptığımızda yeni bir adres doğar
    print("Fonksiyon içi : ",l,id(l))

# ANLAMADIM!!!
benidegistir2(my_list2) # Fonksiyon içi :  [4, 5, 6] 2109026498944
print(my_list2, id(my_list2)) # [1, 2, 3] 2109026499008  # Fonksiyon içindeki değişti, fonksiyon dışındaki sabit kalır
"""
Bir benzetme:
my_list2 bir adres gibi düşün.
Elinde bir kağıt var (my_list2 = [1 , 2, 3]), bu kağıdın üstüne not yazıyorsun.
Fonksiyon içindeyken:
Kalemle üstünü çizip yazı değiştirirsen (my_list2[0] = 10) → Kağıt aynıdır, herkes aynı kağıdı görür.
Ama yeni bir kağıt çıkarıp ona yazarsan (my_list2 = [4  ,5, 6]) → Artık sadece sen o yeni kağıdı görüyorsun, diğerleri hâlâ eskiyi görüyor.
"""


my_list3 = [7, 8, 9]
print(my_list3, id(my_list3)) # [7, 8, 9] 2490050706112

def benidegistir3(l) :
    l += [10, 11, 12]
    print("Fonksiyon içi : ", l, id(l))
benidegistir3(my_list3) # Fonksiyon içi :  [7, 8, 9, 10, 11, 12] 2490050706112
print(my_list3, id(my_list3)) # [7, 8, 9, 10, 11, 12] 2490050706112



# *********************************************************************************************************************



"""
Değer (Value) ve Referans (Reference) Nedir?
Değer (value): bir değişkenin doğrudan bir değeri sakladığı veri tipleridir. 
Referans (reference): bir değişkenin başka bir nesnenin referansını sakladığı veri tipleridir.
Değer Tipleri: Değişkenler doğrudan değer saklar, değişiklikler diğer değişkenleri etkilemez.
Referans Tipleri: Değişkenler nesne referansını saklar, değişiklikler diğer referansları etkiler.

Immutable (Değiştirilemez) Tipler (Değer Gibi Davranır)
Bu tipler değiştirilemez. Bir değişkenin değerini değiştirmeye çalıştığınızda aslında yeni bir nesne oluşturulur.
int, float, bool, str, tuple, frozenset

x = 10
y = x  # y, x'in değerini alır (aynı nesneyi gösterir)
y = 20  # y artık başka bir nesneye referans olur
print(x)  # 10
print(y)  # 20
x ve y başlangıçta aynı nesneyi gösteriyordu, ama y = 20 dediğimizde y artık farklı bir nesneye referans veriyor. x etkilenmez.

Mutable (Değiştirilebilir) Tipler (Referans Gibi Davranır)
Bu tipler değiştirilebilir. Yani bir değişken üzerinden yapılan değişiklik, onu referansla paylaşan diğer değişkenleri de etkiler.
list, dict, set, bytearray

a = [1, 2, 3]
b = a  # b, a ile aynı listeyi gösteriyor (aynı referans)
b.append(4)

print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]
b.append(4) işlemi hem a hem b listesini etkiler çünkü ikisi de aynı listeye referans veriyor.

"""


"""
Değişmez (Immutable) Tipler
Bu tipler değer semantiği gösterir:

int, float, complex (sayısal tipler)
str (string)
tuple
frozenset
bool

Bu tiplerle çalışırken, bir değişkene atama yapıldığında yeni bir nesne oluşturulur:
a = 10
b = a
b = 20
print(a)  # 10 (değişmedi)
print(b)  # 20

x = "merhaba"
y = x
y = "selam"
print(x)  # "merhaba" (değişmedi)


Değişebilir (Mutable) Tipler
Bu tipler referans semantiği gösterir:

list
dict
set
kullanıcı tanımlı sınıflar

Bu tiplerle çalışırken, atama işlemi aynı nesneye referans oluşturur:
liste1 = [1, 2, 3]
liste2 = liste1
liste2.append(4)
print(liste1)  # [1, 2, 3, 4] (değişti!)
print(liste2)  # [1, 2, 3, 4]

# Aynı durum dictionary için:
dict1 = {"a": 1, "b": 2}
dict2 = dict1
dict2["c"] = 3
print(dict1)  # {"a": 1, "b": 2, "c": 3} (değişti!)

Fonksiyon Parametrelerinde Davranış
Python fonksiyonlarda "pass by object reference" kullanır:
"""

"""
Değer (Immutable - Değişmez) Tipler
Bu tipler değiştirilemez (immutable). Bir değişkene yeni bir değer atandığında, aslında yeni bir nesne oluşturulur.

Örnek Değer Tipleri:
Sayılar (int, float, complex)
String (str)
Tuple
Boolean (bool)
Frozenset

Özellikleri:
Değiştirilemezler (immutable)
Fonksiyonlara geçirildiklerinde kopyaları gönderilir
Aynı değere sahip iki değişken aynı bellek adresini gösterebilir (Python'un optimizasyonu)

a = 5
b = a  # b, a'nın değerini alır (yeni bir nesne oluşmaz, aynı bellek adresi)
b = 10  # b'ye yeni değer atanınca yeni bir nesne oluşur

print(a)  # 5 (değişmedi)
print(b)  # 10

Referans (Mutable - Değişebilir) Tipler
Bu tipler değiştirilebilir (mutable). Değişkenler aslında bu nesnelere referans tutar.

Örnek Referans Tipleri:
List
Dictionary
Set
Bytearray
Kullanıcı tanımlı sınıflar

Özellikleri:
Değiştirilebilirler (mutable)
Fonksiyonlara geçirildiklerinde referansları gönderilir
Aynı nesneye referans veren birden fazla değişken olabilir

Örnek:
list1 = [1, 2, 3]
list2 = list1  # list2, list1'in referansını alır (aynı nesneyi gösterir)

list2.append(4)

print(list1)  # [1, 2, 3, 4] (list1 de değişti)
print(list2)  # [1, 2, 3, 4]

Fonksiyonlara Geçirme
Değer tipleri: Fonksiyona kopyası geçer, orijinal değer değişmez
Referans tipleri: Fonksiyona referansı geçer, orijinal nesne değişebilir

def change_num(num):
    num = 10
    print("Fonksiyon içinde:", num)  # 10

Örnek 1 (Değer Tipi):
x = 5
change_num(x)
print("Fonksiyon dışında:", x)  # 5 (değişmedi)

Örnek 2 (Referans Tipi):
def change_list(lst):
    lst.append(4)
    print("Fonksiyon içinde:", lst)  # [1, 2, 3, 4]

my_list = [1, 2, 3]
change_list(my_list)
print("Fonksiyon dışında:", my_list)  # [1, 2, 3, 4] (değişti)

"""




