
if True :
    print("Hoşgeldiniz")

# if False :
#     print("Bu satır çalışmaz")

is_logged_in = True
if is_logged_in :
    print("Hoşgeldiniz")

# if is_logged_in == True : # test için yazdık, bu şekilde anlamsız
#     print("Hoşgeldiniz")

username = "sadikturan"
password = "1234"

is_logged_in = (username == "sadikturan") and (password == "1234") 

if is_logged_in :
    print("Hoşgeldiniz")

if (username == "sadikturan") and (password == "12345") : # değişkene atamadan da yazabiliriz
    print("Hoşgeldiniz")
else :
    print("username ya da password yanlış")

username = "sadikturan"
password = "1234"

if (username == "sadikturan") :
    
    if (password == "1234") :
        print("Hoşgeldiniz")
    else :
        print("password yanlış")

else :
    print("username yanlış")