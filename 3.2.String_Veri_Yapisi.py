
# Karakter dizisi(string veri yapısı) 
# Karakter dizisi denmesinin nedeni birden fazla karakteri olması, karakter grubunun olmasıdır.

name = "Sadık"
surname = "Turan"
age = 36

print('May name is ' + name + ' ' + surname + ' and I am ' + str(age) + ' years old.')
# May name is Sadık Turan and I am 36 years old.

print("My name is " + name + " " + surname + " and \nI am " + str(age) + " years old.")
"""
My name is Sadık Turan and
I am 36 years old.
"""

greeting = "My name is " + name + " " + surname + " and I am " + str(age) + " years old."
print(greeting) # My name is Sadık Turan and I am 36 years old.

"""
String Özellikleri
Değiştirilemez (immutable)	String'ler değiştirilemez.	
Sıralıdır (indexed)	Her karakterin bir indeksi vardır.	
Dilimlenebilir (slicing)	Alt string alınabilir.	
Döngüyle gezilebilir	For döngüsüyle karakter karakter gezilebilir.
"""

print(greeting[0]) # M
print(greeting[2]) # boşluk
print(len(greeting)) # 45

length = len(greeting)
print(greeting[length - 1]) # . (son karakter)
print(greeting[-1]) # . (son karakter)

print(greeting[3 : 7]) # name
print(greeting[3 :]) # name is Sadık Turan and I am 36 years old.
print(greeting[: 16]) # 3 My name is Sadık
print(greeting[2 : 40 : 1]) #  name is Sadık Turan and I am 36 years
print(greeting[2 : 40 : 2]) #  aei aı ua n  m3 er

# String formatlama 

# Eski yöntem .fornat() kullanımı
name = "Çınar"
surname = 'Turan'
print('My name is {} {}.'.format(name, surname)) # My name is Çınar Turan.
print('My name is {0} {1}.'.format(name, surname)) # My name is Çınar Turan.
print('My name is {1} {0}.'.format(name, surname)) # My name is Turan Çınar.
print('My name is {name} {surname}.'.format(name = 'Feride', surname = 'Karakoç')) # My name is Feride Karakoç.
print('My name is {} {} and I am {} years old'.format(name, surname, 36)) # My name is Çınar Turan and I am 36 years old.
name = "Çınar"
surname = 'Turan'
age = 36
print('My name is {} {} and I am {} years old'.format(name, surname, age)) # My name is Çınar Turan and I am 36 years old.
print('My name is {} {} and I am {} years old'.format(name, name, name)) # My name is Çınar Çınar and I am Çınar years old.

result = 200 / 700
print("Result is {}".format(result)) # Result is 0.2857142857142857
print("Result is {r:1.3}".format(r = result)) # Result is 0.286 
print("Result is {r:10.3}".format(r = result)) # Result is      0.286 
# sayının kendisi dahil 10 karakterlik alanda 3 ondalık basamak gösterir

# Yeni yöntem f-string kullanımı
"""
Python'da f-string (tam adıyla formatted string literals), string içine değişken yerleştirmenin en kolay ve modern yoludur. 
Python 3.6 ile gelmiştir ve .format() yöntemine göre daha okunaklı, daha kısa ve hızlıdır.
Çift tırnak " " veya tek tırnak ' ' fark etmez, ama başında f olmak zorunda:
"""

name = "Çınar"
surname = 'Turan'
age = 36
print(f'My name is {name} {surname} and I am {age} years old.') # My name is Çınar Turan and I am 36 years old.
