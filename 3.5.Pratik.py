

website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

result = ' Hello World '.strip
print(result) # Hello World

result = ' Hello World '.lstrip()
print(result) # Hello World

result = ' Hello World '.rstrip()
print(result) #  Hello World

result = website.lstrip("/pth")
print(result)

result = website.lstrip(":/pth")
print(result)

# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.

result = 'www.sadikturan.com'.strip("w.com")
print(result)

# 3- course karakter dizisinin tüm karakterlerini küçük harf yapın.
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
result = course.lower()
print(result) # python kursu: baştan sona python programlama rehberiniz (40 saat)

result = course.upper()
print(result) # PYTHON KURSU: BAŞTAN SONA PYTHON PROGRAMLAMA REHBERINIZ (40 SAAT)

result = course.title()
print(result) # Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)

# 4- website içinde kaç tane a karakteri vardır ? (count('a'))

website = "http://www.sadikturan.com"
result = website.count("a")
print(result) # 2

result = website.count("www")
print(result) # 1

# Aralık belirtebiliriz. Şu aralıkta "www" karakteri kaç kere var?
result = website.count("www", 0 , 10)
print(result) # 1


# 5- website "www" ile başlayıp "com" ile bitiyor mu?
website = "http://www.sadikturan.com"
print(website.startswith("www")) # False
print(website.startswith("http")) # True
print(website.endswith("com")) # True

# 6- 'website' içinde '.com' ifadesi var mı?

result = website.count(".com")
print(result) # 1 # 14 defa geçiyor, yoksa 0 dönerdi



result = website.find(".com")
print(result) # 21 ilk geçtiği indexi verir, yoksa -1 döner

# İstediğimiz bir aralıkta bu değer var mı?
result = website.find(".com", 0 , 10)
print(result) # -1

result = course.find("Python")
print(result) # 0

# Sağdan saymasını istersek, sağdan aramasını istersek
result = course.rfind("Python")
print(result) # 26

result = website.index(".com")
print(result) # 21 ilk geçtiği indexi verir. Yoksa value error verir

result = website.rindex("com")
print(result) # 22


# 7- course içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)

print(course.isalpha()) # False

result = "Hello".isalpha()
print(result) # True

result = course.isdigit()
print(result) # False

result = "123".isdigit()
print(result) # True



# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

result = "Contents".center(50, "*")
print(result) # *********************Contents*********************

# 9- 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.