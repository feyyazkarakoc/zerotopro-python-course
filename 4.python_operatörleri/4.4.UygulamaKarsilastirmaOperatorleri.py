
#1- Girilen 2 sayıdan hangisi büyüktür ?

sayi1 = int(input("Birinci sayıyı giriniz : "))
sayi2 = int(input("İkinci sayıyı giriniz : "))

result = (sayi1 > sayi2)
print(f"Birinci sayı ({sayi1}) ikinci sayı ({sayi2})'dan büyüktür : {result}")

#2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
#   Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

vize1 = float(input("Birinci vize : "))
vize2 = float(input("İkinci vize : "))
final = float(input("Final : "))
ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)
result = f"not ortalamanız : {ortalama} ve dersten geçme durumunuz : {ortalama >= 50})"
print(result)

#3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.

sayi = int(input("Bir sayı giriniz : "))
result = sayi % 2 == 0
print(f"Girdiğiniz {sayi} sayısı çifttir : {result}")

#4- Girilen bir sayının negatif pozitif durumunu yazdırın.

sayi = int(input("Bir sayı giriniz : "))
pozitifmi = (sayi > 0)
print(f"Girdiğiniz {sayi} sayısı pozitiftir : {pozitifmi} ")

#5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz. 
# (email: email@sadikturan.com parola: abc123)

email = "email@sadikturan.com"
password = "abc123"

girilen_email = input("email : ").lower().strip()
girilen_password = input("parola : ")

is_email = (email == girilen_email)
is_password = (password == girilen_password)

print(f"Girilen email bilgisi doğru mu : {is_email}, girilen parola doğru mu : {is_password}")

