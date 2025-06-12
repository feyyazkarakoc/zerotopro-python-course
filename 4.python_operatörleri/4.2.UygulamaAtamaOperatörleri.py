

x, y, z = 2, 5, 10
numbers = 1, 5, 7, 10, 6

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir 

sayi1 = int(input("Birinci sayıyı giriniz : "))
sayi2 = int(input("İkinci sayıyı giriniz : "))

result = (sayi1 * sayi2) - (x+ y+ z)
print(result)

# 2- y' nin x' e kalansız bölümünü hesaplayınız.

result = y // x
print(result) # 2

#3- (x,y,z) toplamının mod 3' ü nedir ?

result = (x + y + z) % 3
print(result) # 2

# 4- y' nin x. kuvvetini hesaplayınız.

result = y ** x
print(result) # 25

#5- x, *y, z = numbers işlemine göre z' nin küpü kaçtır ?

x, *y, z = numbers
result = z ** 3
print(y) # [5, 7, 10]
print(z) # 6
print(result) # 216

# 6- x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır ?

print(y) # [5, 7, 10]
result = sum(y)
print(result) # 22

result = y[0] + y[1] + y[2]
print(result) # 22