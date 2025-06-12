""""
Java Dosya Uzantısı: .java
Java'da tüm kaynak kod dosyaları .java uzantısıyla biter.
Bu dosyanın içinde bir class, interface, enum, veya record olabilir.
IntelliJ IDEA gibi IDE'ler, sol panelde dosya uzantılarını gizleyebilir ama arka planda hepsi .java uzantılıdır.

Python Dosya Uzantısı: .py
Python'da tüm kaynak kod dosyaları .py uzantılıdır.
Dosya içinde fonksiyon, sınıf vs. olabilir ama fark etmez, uzantı hep .py'dir.
"""




"""
>>> işareti ise Python yorumlayıcısının komut beklediğini gösteriyor (REPL ortamı).
Python REPL ortamından çıkmak için:
exit() yazıp Enter’a bas


"""

"""
PowerShell'de Python başlatıp >>> gibi bir Python etkileşimli terminaline (REPL) geçtiğinizde, artık PowerShell 
komutları yazamazsınız. Sen şu an Python ortamındasın ve orada python --version gibi bir komut geçersizdir çünkü 
bu bir Python ifadesi değil, bir terminal (PowerShell) komutudur. Bu yüzden şu hatayı alıyorsun:
NameError: name 'python' is not defined
Doğru Kullanım
Eğer PowerShell'deysen:
PowerShell terminalinde doğrudan şu komutu yaz:
python --version
veya
python -V
Eğer Python ortamındaysan (>>> görünüyorsa):
Bu durumda PowerShell'e geri dönmek için önce Python REPL'den çıkman gerekir. Çıkmak için:
exit()
veya
quit()
yaz, Enter'a bas. Ardından PowerShell'e döndüğünde python --version komutunu çalıştırabilirsin.
Özetle:
>>> varsa, Python ortamındasın, terminal komutları burada çalışmaz.
python --version gibi komutlar sadece PowerShell'de yazılmalı.
Python'dan çıkmak için exit() kullan.
"""

"""
VS Code kullanırken .png dosyalarının GitHub’a yüklenmesini istemiyorsan, bunları Git izleme dışı bırakman gerekir. 
Bunu .gitignore dosyasıyla yapabilirsin.
1. .gitignore Dosyasına .png Ekle
Proje dizininde .gitignore dosyasını aç (yoksa oluştur) ve içine şunu yaz:
*.png
Bu, tüm .png dosyalarının Git tarafından izlenmesini engeller.
Not: Bu işlem sadece yeni eklenen .png dosyaları için geçerlidir. Daha önce Git'e eklenmiş olan .png dosyalarını etkilemez.
2. Daha Önce Eklenmiş .png Dosyaları için
Eğer .png dosyaları daha önce commit edildiyse, onları takipten çıkarmak için şu adımları izleyebilirsin:
Terminalde:
git rm --cached *.png
Bu, .png dosyalarını repo geçmişinden silmez, sadece bir sonraki commit'te izleme dışı bırakır.
Sonra tekrar commit et:
git commit -m "Remove PNG files from tracking"
"""