

# 1- "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.

arabalar = ["Bmw", "Mercedes", "Opel", "Mazda"]

# 2- Liste Kaç elemanlıdır ?

result = len(arabalar)
print(result) # 4

# 3- Listenin ilk ve son elemanı nedir ? 

first = arabalar[0]
end = arabalar[len(arabalar) - 1]
print(first, end) # Bmw Mazda

first = arabalar[0]
end = arabalar[-1]
print(first, end) # Bmw Mazda

# 4- Mazda değerini Toyota ile değiştirin.

# string immutable, listeler mutable
arabalar[-1] = "Toyota"
print(arabalar) # ['Bmw', 'Mercedes', 'Opel', 'Toyota']

# 5- Mercedes listenin bir elemanı mıdır ? 

result = "Mercedes" in arabalar
print(result) # True

# 6- Listenin -2 indeksindeki değer nedir ?

print(arabalar[-2]) # Opel

# 7- Listenin ilk 3 elemanını alın.

result = arabalar[0 : 3]
print(result) # ['Bmw', 'Mercedes', 'Opel']
print(arabalar[:3]) # ['Bmw', 'Mercedes', 'Opel']


# 8- Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.

arabalar = ["Bmw", "Mercedes", "Opel", "Mazda"]
arabalar[-2 : ] = ["Toyota", "Renault"]
print(arabalar)

# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.

arabalar = arabalar + ["Audi", "Nissan"]
print(arabalar) # ['Bmw', 'Mercedes', 'Toyota', 'Renault', 'Audi', 'Nissan']

# 10- Listenin son elemanını silin.

del arabalar[-1]
print(arabalar) # ['Bmw', 'Mercedes', 'Toyota', 'Renault', 'Audi']

# 11- Liste elemanlarını tersten yazdırınız.

result = arabalar[: : -1]
print(result) # ['Audi', 'Renault', 'Toyota', 'Mercedes', 'Bmw']

# 12- Aşağıdaki verileri bir liste içinde saklayınız.
# studentA: Yiğit Bilgi 2010, (70,60,70) 
# studentB: Sena Turan 1999, (80,80,70) 
# studentC: Ahmet Turan 1998, (80,70,90)

studentA = ["Yiğit", "Bilgi", 2010, [70,60,70]]
studentB = ["Sena", "Turan", 1999, [80,80,70]] 
studentC = ["Ahmet", "Turan", 1998, [80,70,90]]

# 13- Liste elemanlarını ekrana yazdırınız.

result = studentA[0]
print(result) # Yiğit

result = studentB[1]
print(result) # Turan

result = studentC[3][1]
print(result) # 70

# Yiğit Bilgi 15 yaşında ve not ortalaması 66'dır. 
result = f"{studentA[0]} {studentA[1]}, {2025 - studentA[2]} yaşında ve not ortalaması {((studentA[3][0] + studentA[3][1] + studentA[3][2])/3):.2f}'dır."
print(result) # Yiğit Bilgi, 15 yaşında ve not ortalaması 66.67'dır.

