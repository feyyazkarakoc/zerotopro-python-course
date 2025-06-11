
# Sayısal veri tipleri integer ve float

print(2 + 1)
"""
Terminale py 3.Python_Objeleri_Ve_Veri_Yapılari.py yazıp çalıştırıyoruz, burda hata verdi,
python "3.Python_Objeleri_Ve_Veri_Yapılari.py" ile çalıştırdık.

""" 

print(2 + 1.5) # 3.5
print(2.0 + 5.0) # 7.0

print(type(2.0)) # <class 'float'>
print(type(2)) # <class 'int'>

print(2 + 10 * 10 + 8) # 110

print((2 + 10) * 10 +8) # 128

print((2 + 10) * (10 + 8)) # 216


# Matematiksel Operatörler

print(4 - 0.5) # 3.5
print(0.5 * 2) # 1.0
print(1 / 2) # 0.5
print(20 / 2) # 10.0
print(2 ** 3) # 8
print(3 ** 4) # 81
print(3 ** 0.5) # 1.7320508075688772
print(10 % 2) # 0
print(11 % 2) # 1
print(12345852147 % 6) # 3
print(10 / 3) # 3.3333333333333335
print(10 // 3) # 3
print(15 // 4) # 3
print(-15 // 4) # -4 !!!DİKKAT
print(-10 // 3) # -4 !!!DİKKAT

# Değişken tanımlama
maasAhmet = 5000
maasAli = 4000
vergi = 0.27
print(maasAhmet - (maasAhmet * vergi)) # 3650.0
print(maasAli - (maasAli * vergi)) # 2920.0

# Değişken tanımlama kuralları
# rakam iile başlayamaz
# Değişken tanımladığımızda değerini atamak zorundayız

number1 = 10
print(number1) # 10

number1 = 20
print(number1) # 20

number1 += 30
print(number1) # 50

# Büyük küçük harf duyarlılığı vardır

age = 10
AGE = 50
print(age) # 10
print(AGE) # 50

# Türkçe karakter kullanmayalım
yas = 25 

x = 1             # int
y = 2.3           # float
name = "Çınar"    # string
isStudent = True  # bool

x, y, name, isStudent = 1, 2.3, "Çınar", True #!!!DİKKAT

a = 10
b = 20
print(a + b) # 30

a = '10'
b = '20'
print(a + b) # 1020, string olarak birleştirme yapar

firstName = "Sadık"
lastName = "Turan"
print(firstName + " " + lastName) # Sadık Turan

"""

1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.
Müşteri adı
Müşteri soyadı
Müşteri ad + soyad
Müşteri cinsiyet
Müşteri tc kimlik
Müşteri doğum yılı 
Müşteri adres bilgisi
Müşteri yaşı
"""

musteriAdi = "Ali"
musteriSoyad = "Yılmaz"
musteriAdSoyad = musteriAdi + " " + musteriSoyad
musteriCinsiyet = True # True: Erkek, False: Kadın 
musteriTcKimlik = '12345678912'
musteriDogumYili = '1989'
musteriAdresi = "İstanbul Kadıköy"
musteriYasi = 2025 - int(musteriDogumYili)

print(musteriYasi) # 36

"""
2- Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.
Sipariş 1 => 110 TL
Sipariş 2 => 1100.5 TL
Sipariş 3 => 356.95 TL
"""

print(110 + 1100.5 + 356.95) # 1567.45

order1 = 110
order2 = 1100.5
order3 = 356.95
print(order1 + order2 + order3) # 1567.45

total = order1 + order2 + order3
print("Total : ",total) # Total :  1567.45

# Veri Tipi Dönüşümleri (Type Conversion)
x = input("Birinci sayıyı giriniz: ") # 10 # input her zaman string olarak alır
y = input("İkinci sayıyı giriniz: ") # 20 # input her zaman string olarak alır

toplam = x + y
print("Toplam : ", toplam) # Toplam : 1020

print(type(x)) # <class 'str'>
print(type(y)) # <class 'str'>
toplam = int(x) + int(y)
print("Toplam : ",toplam) # Toplam : 30
print(type(toplam)) # <class 'int'>

# Hepsini yorum satırına dönüştürmek için Ctrl + K + C

x = 5             # int
y = 2.5           # float
name = "Çınar"    # str
isOnline = True   # bool

print(type(x), type(y), type(name), type(isOnline)) # <class 'int'> <class 'float'> <class 'str'> <class 'bool'>

# int to float
x = float(x) 
print(x) # 5.0
print(type(x)) # <class 'float'>

# float to int
y = int(y)
print(y) # 2
print(type(y)) # <class 'int'>

result = x + y
print(result) # 7.0 #!!!
print(type(result)) # <class 'float'>

# int/float to str
result = str(x) + str(y)
print(result) # 5.02
print(type(result)) # <class 'str'>

# bool to str
isOnline = str(isOnline)
print(isOnline) # True
print(type(isOnline)) # <class 'str'>

# bool to int
isOnline = True 
isOnline = int(isOnline) 
print(isOnline) # 1
print(type(isOnline)) # <class 'int'>


"""

Daire Alanı : r2
Daire Çevresi : 2лr
Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız. (л : 3.14)
"""
r = float(input("Yarı çapı giriniz: ")) 
л = 3.14
cevre = 2 * л * r
alan = л * (r ** 2)

print(f"Dairenin çevresi : {cevre:.2f}\nDairenin alanı : {alan:.2f}")

print("Çevre : " + cevre + "Alan : " + alan) # TypeError: can only concatenate str (not "float") to str
# Doğru kullanım
print("Çevre : " + str(cevre) + " Alan : " + str(alan)) # Çevre : 18.84 Alan : 28.26







