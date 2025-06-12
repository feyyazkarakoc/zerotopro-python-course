"""
Komut istemi programı, kullanıcının bilgisayara metin tabanlı komutlar yazarak çeşitli işlemler yapmasını sağlayan bir yazılımdır.
Bu tür programlar genellikle grafik arayüz (GUI) yerine bir yazı ekranı (konsol/terminal) üzerinden çalışır.
Basit Tanımıyla:
Kullanıcının komutlar yazarak bilgisayarla etkileşim kurduğu, metin tabanlı bir programdır.
Örnekler:
Komut İstemi Programı	       Platform	         Açıklama
CMD (Command Prompt)	       Windows	         dir, cd, copy gibi komutlarla dosya işlemleri yapılır.
PowerShell	                   Windows	         CMD’ye göre daha gelişmiş betik desteği sağlar.
Terminal (Bash/Zsh)	           macOS / Linux	 ls, cd, grep, chmod, sudo gibi komutlar kullanılır.

"""





"""
Hata, PowerShell komut satırında mkdir komutuyla klasör ismi oluştururken boşluklu isimleri doğrudan yazmanızdan kaynaklanıyor. 
PowerShell boşlukları ayrı parametre olarak algılar, bu da hataya neden olur.
Doğru Kullanım
Klasör ismi boşluk içeriyorsa çift tırnak (") veya tek tırnak (') içine almalısınız:
mkdir "SIFIRDAN ILER SEVIYE PYTHON"
veya
mkdir 'SIFIRDAN ILER SEVIYE PYTHON'
PowerShell'de boşluk karakteri, birden fazla argümanı ayırmak için kullanılır.
mkdir SIFIRDAN ILER SEVIYE PYTHON komutu, mkdir komutuna 4 farklı parametre vermiş gibi algılanır. Ancak mkdir bu kadar parametre beklemez.
"""

"""
ls yerine kullanılabilecek komutlar:
dir	CMD uyumlu eşdeğeridir
"""

"""
PowerShell veya Komut İstemi (CMD) kullanırken D: sürücüsüne geçmek için cd komutu tek başına yeterli değildir, çünkü cd sadece mevcut
sürücüdeki klasörü değiştirir, sürücüyü değiştirmez.
Doğru Yöntem: Sürücü Değiştirmek için
D:
Bu kadar. Sadece D: yaz ve Enter'a bas.
"""

"""
Bir üst klasöre çıkmak	cd ..
İki klasör yukarı çıkmak	cd ..\..
Ana dizine dönmek	cd \
Tüm yolu yazarak geçmek	cd D:\Yol\AltKlasör
Aynı anda sürücü de değiştirmek (CMD)	cd /d D:\Yol\AltKlasör

PowerShell'de /d gerekmez, sadece cd D:\Yol\AltKlasör yeterlidir.
"""

"""
Terminalde (PowerShell) bulunduğun konumu değiştirmek için cd (change directory) komutunu kullanırsın.
cd — Change Directory
Amacı: Klasör (dizin) değiştirmek.

dir — Directory
Amacı: Bulunduğun klasördeki tüm dosya ve klasörleri listelemek.

mkdir — Make Directory
Anlamı: Yeni bir klasör (dizin) oluşturmak için kullanılır.

"""

"""
Klasördeki dosya ve klasörleri görmek için:
dir
(veya ls de yazabilirsin, çalışır)
"""