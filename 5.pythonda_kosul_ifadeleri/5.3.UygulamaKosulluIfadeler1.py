

# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme 
# durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu 
# lise ya da üniversite olmalıdır.

isim = input("isminiz : ")
yas = input("yaşınız : ")
egitim = input("eğitim : ")

result = (yas >= 18) and (egitim == "lise" or  egitim == "üniversite")



# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre 
# not aralığına karşılık gelen not bilgisini yazdırınız.
# 0 -24 => 0
# 25-44 => 1
# 45-54 => 2
# 55-69 => 3
# 70-84 => 4
# 85-100 => 5

# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
# göre hesaplayınız.
# 1. Bakım => 1. yıl
# 2. Bakım => 2. yıl
# 3. Bakım => 3. yıl
# ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız
# *** datetime modülünü kullanmamız gerekiyor