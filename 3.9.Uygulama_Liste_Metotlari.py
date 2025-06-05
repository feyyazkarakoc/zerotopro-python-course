

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

# 4- "Deniz" isminin indeksi nedir ?
# 5- "Ali" listenin bir elemanı mıdır?
# 6-  Liste elemanlarını ters çevirin.
# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
# 8-  years listesini rakamsal büyüklüğe göre sıralayınız.
# 9-   str = "Chevrolet, Dacia" karakter dizisini listeye çeviriniz.
# 10- years dizisinin en büyük ve en küçük elemanı nedir ?
# 11- years dizisinde kaç tane 1998 değeri vardır ?
# 12- years dizisinin tüm elemanlarını siliniz.
# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız."""