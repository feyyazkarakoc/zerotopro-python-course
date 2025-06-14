
# identity operator : is

x = y = [1, 2, 3]

z = [1, 2, 3]

print(x == y) # True
print(x == z) # True # == operatörü değer karşılaştırması yapar. Her iki listenin içeriği [1, 2, 3] olduğu için eşittir.

# Değer karşılaştırması değil de, referans tipindeki verilerin adres karşılaştırmasını yaparsak x ve y aynı adreste olur
print(x is y) # True 

# is aynı obje mi diye bakar
# x ve z içerikleri aynı olsa bile farklı referanslara sahip. 
# is opratörünü kullanırken değer önemli değil, aynı adresi tutup tutmadığı önemli
print(x is z) # False

print(id(x), id(y), id(z)) # 1126544936896 1126544936896 1126546406848

x = [1, 2, 3]
y = [2, 4]

print(x == y) 
print(x is y) # False

del x[2]
y[1] = 1
y.reverse()
print(x == y) # True 
print(x is y) # False # Referansları ayrı, bellekte iki farklı adreste yer alırlar
print(x is not y) # True 

# membership operator : in

x = ["apple", "banana"]
print("banana" in x) # True 

name = "Çınar"
print('a' in name) # True 
print("a" not in name) # False 
