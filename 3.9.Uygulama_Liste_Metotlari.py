

names = ['Ali', 'Yağmur', 'Hakan', 'Deniz'] 
years = [1998, 2000, 1998, 1987]

# 1- "Cenk" ismini listenin sonuna ekleyiniz.

names.append("Cenk")
print(names) # ['Ali', 'Yağmur', 'Hakan', 'Deniz', 'Cenk']

# 2- "Sena" değerini listenin başına ekleyiniz.

names.insert(0, "Sena")
print(names) # ['Sena', 'Ali', 'Yağmur', 'Hakan', 'Deniz', 'Cenk']

names.insert(-1, "Mehmet")
print(names) # ['Sena', 'Ali', 'Yağmur', 'Hakan', 'Deniz', 'Mehmet', 'Cenk']

# en sona eklemek istersek
names.insert(len(names), "Feyyaz")
print(names) # ['Sena', 'Ali', 'Yağmur', 'Hakan', 'Deniz', 'Mehmet', 'Cenk', 'Feyyaz']

# 3- "Deniz" ismini listeden siliniz.

names.remove("Deniz")
print(names) # ['Sena', 'Ali', 'Yağmur', 'Hakan', 'Mehmet', 'Cenk', 'Feyyaz']

names.pop()
print(names) # ['Sena', 'Ali', 'Yağmur', 'Hakan', 'Mehmet', 'Cenk']

names.pop(1)
print(names) # ['Sena', 'Yağmur', 'Hakan', 'Mehmet', 'Cenk']

# 4- "Yağmur" isminin indeksi nedir ?

index = names.index("Yağmur")
print(index) # 1

names.pop(index)
print(names) # ['Sena', 'Hakan', 'Mehmet', 'Cenk']


# 5- "Ali" listenin bir elemanı mıdır?

result = "Ali" in names
print(result) # False

result = names.index("Ali")
print(result) # ValueError: 'Ali' is not in list

# 6-  Liste elemanlarını ters çevirin.

print(names) # ['Sena', 'Hakan', 'Mehmet', 'Cenk']

result = names[: : -1]
print(result) # ['Cenk', 'Mehmet', 'Hakan', 'Sena']

names.reverse()
print(names) # ['Cenk', 'Mehmet', 'Hakan', 'Sena']

result = sorted(names, reverse = True)
print(result) # ['Sena', 'Mehmet', 'Hakan', 'Cenk']

# 7-  Liste elemanlarını alfabetik olarak sıralayınız.

print(names) # ['Cenk', 'Mehmet', 'Hakan', 'Sena']

result = sorted(names)
print(result) # ['Cenk', 'Hakan', 'Mehmet', 'Sena']

print(names) # ['Cenk', 'Mehmet', 'Hakan', 'Sena']
names.sort()
print(names) # ['Cenk', 'Hakan', 'Mehmet', 'Sena']


"""
Python'da fonksiyon (function) ve metot (method) kavramları benzer gibi görünse de temelde farklıdır.
Fonksiyon:
Bağımsızdır, herhangi bir nesneye bağlı değildir.
Doğrudan çağrılır: fonksiyon_adı().
Örnek: sorted(), len(), print().

Metot:
Bir nesneye (object) bağlıdır.
Belirli bir veri tipi (liste, string, sözlük vb.) ile kullanılır.
Nesne üzerinden çağrılır: nesne.metot_adı().
Örnek: liste.sort(), string.upper().


Fonksiyon:
Modül içinde veya genel alanda tanımlanır.
Örneğin:
python
def kare_al(x):
    return x ** 2

Metot:
Bir sınıf (class) içinde tanımlanır ve o sınıfın nesnelerine aittir.
Örneğin:
python
class Araba:
    def calis(self):
        print("Motor çalıştı!")

Fonksiyon:
Genellikle argüman alır ve sonuç döndürür.
Örnek: len(names) → 3 (names'in uzunluğunu verir).

Metot:
İlk parametresi genelde self'tir (nesnenin kendisi).
Bazı metotlar orijinal nesneyi değiştirir (sort()), bazıları yeni değer döndürür (string.upper()).
"""

# 8-  years listesini rakamsal büyüklüğe göre sıralayınız.

print(years) # [1998, 2000, 1998, 1987]

result = sorted(years)
print(result) # [1987, 1998, 1998, 2000]

print(years) # [1998, 2000, 1998, 1987]
years.sort()
print(years) # [1987, 1998, 1998, 2000]

# 9-   str = "Chevrolet, Dacia" karakter dizisini listeye çeviriniz.

str = "Chevrolet, Dacia"
result = str.replace(" ","").split(",")
print(result) # ['Chevrolet', 'Dacia']

# 10- years dizisinin en büyük ve en küçük elemanı nedir ?

print(years) # [1987, 1998, 1998, 2000]

result = max(years)
print(result) # 2000

result = min(years)
print(result) # 1987

# 11- years dizisinde kaç tane 1998 değeri vardır ?

print(years)
result = years.count(1998)
print(result) # 2

# 12- years dizisinin tüm elemanlarını siliniz.

years.clear()
print(years) # []

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız."""

markalar = []

marka = input("Marka : ")
markalar.append(marka)

marka = input("Marka : ")
markalar.append(marka)

marka = input("Marka : ")
markalar.append(marka)

print(markalar)


