

# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz. 

sayi = int(input("Bir sayı giriniz : "))
result = (sayi > 0) and (sayi <= 100)
print(f"Girilen {sayi} sayısı 0 ile 100 arasındadır : {result}")

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

sayi = int(input("Bir sayı giriniz : "))
result = (sayi > 0) and (sayi % 2 == 0)
print(f"Girilen {sayi} sayısı pozitif çift sayı mı : {result}")

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.

email = "sadikturan@gmail.com"
parola = "123abc"

girilen_email = input("Email giriniz : ")
girilen_parola = input("Parola giriniz : ")

result = (girilen_email == email) and (girilen_parola == parola)
print(f"Uygulamaya giriş başarılı mı : {result}")


# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

a = int(input("Birinci sayıyı giriniz : "))
b = int(input("İkinci sayıyı giriniz : "))
c = int(input("Üçüncü sayıyı giriniz : "))

result = (a > b) and (a > c)
print(f"{a} en büyük sayıdır : {result} ")

result = (b > a) and (b > c)
print(f"{b} en büyüktür sayıdır: {result}")

result = (c > a) and (c > b)
print(f"{c} en büyüktür sayıdır: {result}")

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız 

vize1 = float(input("Birinci vize : "))
vize2 = float(input("İkinci vize : "))
final = float(input("Final : "))
ortalama = ((vize1 + vize2) / 2) * 0.6 + final * 0.4

#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.

result = (ortalama >= 50) and (final >= 50)
print(f"Öğrencinin ortalaması : {ortalama} ve geçme durumu : {result}")

#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.

result = (ortalama >= 50) or (final >= 70)
print(f"Öğrencinin ortalaması : {ortalama} ve geçme durumu : {result}")

# 6- Kişinin ad, kilo ve boy bilgilerini alıp vücut kitle indekslerini(Body Mass Index (BMI)) hesaplayınız. 
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4 => Zayıf
#    18.5-24.9 => Normal
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)

name = input("Adınız : ")
weight = float(input("Kilonuz(kg) : "))
height = float(input("Boyunuz(m) : "))
bmi = weight / (height ** 2)

is_underweight = (bmi >= 0) and (bmi <= 18.4)
is_normal = (bmi > 18.4) and (bmi <= 24.9)
is_overweight = (bmi > 24.9) and (bmi <= 29.9)
is_obese = (bmi > 29.9) and (bmi <= 34.9)

print(f"{name} vücut kitle indexi : {bmi}, zayıf mı : {is_underweight}, normal mi : {is_normal}, kilolu mu : {is_overweight}, obez mi : {is_obese} ")

