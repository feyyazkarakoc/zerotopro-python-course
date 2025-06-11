
list = [1, 2, 3]

tuple = 1, "iki", 3
#veya
tuple = (1, "iki", 3)

print(type(list)) # <class 'list'>
print(type(tuple)) # <class 'tuple'>
print(type(tuple)) # <class 'tuple'>

print(list[2]) # 3
print(tuple[2]) # 3

print(len(list)) # 3
print(len(tuple)) # 3

list = ["ali", "veli"] 
tuple = ("damla", "ayşe")

print(list) # ['ali', 'veli']
print(tuple) # ('damla', 'ayşe')

list[0] = "ahmet"
print(list) # ['ahmet', 'veli']

tuple[0] = "deniz" # TypeError: 'tuple' object does not support item assignment
print(tuple) # ('damla', 'ayşe')

tuple = ('damla', 'ayşe', 'ayşe')
print(tuple.count("ayşe")) # 2

print(tuple.index("ayşe")) # 1

names = ("demet", "emel", "ayşe") + tuple
print(names) # ('demet', 'emel', 'ayşe', 'damla', 'ayşe', 'ayşe')
