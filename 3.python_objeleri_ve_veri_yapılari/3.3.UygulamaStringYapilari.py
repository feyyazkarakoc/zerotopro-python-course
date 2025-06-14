
website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?

result = len(course)
print(result) # 65

# 2- 'website' içinden www karakterlerini alın.

result = website[7 : 10]
print(result) # www

result = website[-18 : -15]
print(result) # www


# 3- 'website' içinden com karakterlerini alın.

result = website[-3 :]
print(result) # com

result = website[22 :]
print(result) # com

result = website[22 : 25]
print(result) # com

result = website[len(website) - 3 :]
print(result) # com

length = len(website)
result = website[length - 3 : length]
print(result) # com

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın. 

print(course[:15] + " " + course[len(course) - 15 :])
# Python Kursu: Ba riniz (40 saat)

print(course[0 : 15] + " " + course[-15 :])
# Python Kursu: B riniz (40 saat)


#5- 'course' ifadesindeki karakterleri tersten yazdırın.

print(course[: : ]) # Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)
print(course[: : 1]) # Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)
print(course[: : -1]) # )taas 04( zinirebheR amalmargorP nohtyP anoS natşaB :usruK nohtyP

s = "12345" * 5
print(s) # 1234512345123451234512345
print(s[: : 5]) # 11111



name, surname, age, job = 'Bora', 'Yılmaz', 32, 'mühendis'
# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın: 
# 'Benim adım Bora Yılmaz, yaşım 32 ve mesleğim mühendis.'

print(f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}.")
# Benim adım Bora Yılmaz, yaşım 32 ve mesleğim mühendis.

result = "Benim adım " + name + " " + surname + ", yaşım " + str(age) + " ve mesleğim " + job + "."
print(result) # Benim adım Bora Yılmaz, yaşım 32 ve mesleğim mühendis.

result = "Benim adım {0} {1}, yaşım {2} ve mesleğim {3}.".format(name, surname, age, job)
print(result) # Benim adım Bora Yılmaz, yaşım 32 ve mesleğim mühendis.

# 7- 'Hello World' ifadesindeki w harfini W harfi ile değiştirin.

s = 'Hello World'
s[6] = 'W' # TypeError: 'str' object does not support item assignment
print(s)

s = 'Hello World'
result = s[0 : 6] + 'W' + s[7 :]
print(result)

s = 'Hello World'
result = s[0 : 6] + 'W' + s[-4 :]
print(result) # Hello World

result = s.replace("w","W")
print(result) # Hello World

# 8 - 'abc' ifadesini 3 kere yan yana yazdırın.

print("abc"* 3) # abcabcabc