
message = 'Hello There. My name is Sadık Turan'

print(message) # Hello There. My name is Sadık Turan

message = message.upper()
print(message) # HELLO THERE. MY NAME IS SADIK TURAN

message = message.lower()
print(message) # hello there. my name is sadik turan

message = message.title()
print(message) # Hello There. My Name Is Sadik Turan

message = message.capitalize()
print(message) # Hello there. my name is sadik turan
"""
Python'daki .capitalize() metodu:
String'in ilk harfini büyük yapar.
Diğer tüm harfleri küçük yapar.
"""

"""
title() metodu:
Tüm kelimeleri tespit eder (boşluklara göre ayırır).
Her kelimenin ilk harfini büyütür.
O kelimenin geri kalan tüm harflerini küçültür.
"""


"""
strip()	Baştaki ve sondaki boşlukları/karakterleri siler
lstrip()	Sadece baştaki boşlukları/karakterleri siler
rstrip()	Sadece sondaki boşlukları/karakterleri siler
"""

message = '  Hello There. My name is Sadık Turan  '
message = message.strip()
print(message) # Hello There. My name is Sadık Turan

message = 'xxxHello There. My name is Sadık Turanxxxx'
print(message.strip("x")) # Hello There. My name is Sadık Turan

"""
split() metodu, bir string'i belirli bir ayırıcıya (separatör) göre parçalara ayırır 
ve bu parçaları bir liste (list) olarak döndürür.
str.split(sep=None, maxsplit=-1)
sep : Ayırıcı karakter veya string (örneğin ".", ",", "-" vs.)
maxspli : En fazla kaç defa bölüneceğini belirtir. Varsayılan -1 (sınırsız).
"""

message = 'Hello There. My name is Sadık Turan'
print(message.split()) # ['Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan']
print(message.split(".")) # ['Hello There', ' My name is Sadık Turan']

"""
join() metodu, bir liste (veya benzeri dizilerdeki) string’leri alır ve bunları belirttiğin bir 
ayırıcıyla birleştirerek tek bir string haline getirir.
"""
message = 'Hello There. My name is Sadık Turan'
message = message.split()
print(message) # ['Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan']
message = " ".join(message)
print(message) # Hello There. My name is Sadık Turan

message = 'Hello There. My name is Sadık Turan'
message = message.split()
message = "---".join(message)
print(message) # Hello---There.---My---name---is---Sadık---Turan


"""
find() metodu, bir string içinde başka bir string'in ilk geçtiği yeri (indeksini) bulmak için kullanılır.
str.find(sub[, start[, end]]) -> int
Parametreler:
sub → Aranacak alt string.
start → (İsteğe bağlı) Aramaya başlanacak indeks.
end → (İsteğe bağlı) Aramanın biteceği indeks (son dahil değil).
Eğer sub bulunursa: ilk geçtiği indeks (int)
Eğer sub bulunmazsa: -1

find() → Bulamazsa -1 döner.
index() → Bulamazsa ValueError hatası verir.
"""

message = 'Hello There. My name is Sadık Turan'
print(message.find("Sadık")) # 24
print(message.index("S")) # 24
print(message.find("Sadıkx")) # -1 # Aranılan kelime yoksa -1 döner

"""
str.startswith(prefix[, start[, end]]) -> bool
prefix → Başta olup olmadığını kontrol etmek istediğin ifade (string, tuple of strings olabilir).
start → (Opsiyonel) Aramaya başlanacak indeks.
end → (Opsiyonel) Aramanın biteceği indeks (son dahil değil).

True → Eğer string belirtilen ifade ile başlıyorsa
False → Aksi halde
"""

message = 'Hello There. My name is Sadık Turan'
isFound = message.startswith("H")
print(isFound) # True

isFound = message.startswith("B")
print(isFound) # False

isFound = message.endswith("n")
print(isFound) # True

"""
str.replace(old, new, count=-1)
old → Değiştirilecek alt string.
new → Yerine konacak alt string.
count (opsiyonel) → En fazla kaç tane değişiklik yapılacağını belirtir. Varsayılanı -1, yani hepsini değiştir.

Yeni bir string döner. (Orijinal string değişmez, çünkü string'ler immutable’dır.)
"""

message = 'Hello There. My name is Sadık Turan'
message = message.replace("Sadık", "Feyyaz")
print(message) # Hello There. My name is Feyyaz Turan
message = message.replace("ç", "c").replace("ö", "o").replace(" ", "-")
print(message) # Hello-There.-My-name-is-Feyyaz-Turan

