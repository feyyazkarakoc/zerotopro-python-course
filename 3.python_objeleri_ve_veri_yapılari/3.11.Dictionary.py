
# key - value

sehirler = ["kocaeli", "istanbul"]
plakalar = [41, 34]

print(plakalar[sehirler.index("kocaeli")]) # 41
print(plakalar[sehirler.index("istanbul")]) # 34

plakalar = {"kocaeli" : 41,  "istanbul" : 34}
print(plakalar) # {'kocaeli': 41, 'istanbul': 34}
print(plakalar["kocaeli"]) # 41
print(plakalar["istanbul"]) # 34

plakalar["ankara"] = 6
print(plakalar) # {'kocaeli': 41, 'istanbul': 34, 'ankara': 6}

plakalar["kocaeli"] = "new value"
print(plakalar) # {'kocaeli': 'new value', 'istanbul': 34, 'ankara': 6}


users = {
    "sadıkturan" : 36,
    "cınarturan" : 2
}

print(users["cınarturan"]) # 2

users = {
    "sadıkturan" : {
        "age" : 36,
        "email" : "sadik@gmail.com",
        "adress" : "kocaeli",
        "phone" : "1231231"
    }, 
    "cınarturan" : {
        "age" : 2,
        "email" : "cinar@gmail.com",
        "adress" : "kocaeli",
        "phone" : "1231231"

    }
}

print(users["cınarturan"]) # {'age': 2, 'email': 'cinar@gmail.com', 'adress': 'kocaeli', 'phone': '1231231'}
print(users["cınarturan"]["age"]) # 2
print(users["cınarturan"]["email"]) # cinar@gmail.com
print(users["cınarturan"]["adress"]) # kocaeli

users = {
    "sadıkturan" : {
        "age" : 36,
        "roles" : ["user"],
        "email" : "sadik@gmail.com",
        "adress" : "kocaeli",
        "phone" : "1231231"

    },
    "cınarturan" : {
        "age" : 2,
        "roles" : ["admin", "user"],
        "email" : "cinar@gmail.com",
        "adress" : "kocaeli",
        "phone" : "1231231"

    }
}

print(users["cınarturan"]["roles"][0]) # admin
print(users["cınarturan"]["roles"][1]) # user


