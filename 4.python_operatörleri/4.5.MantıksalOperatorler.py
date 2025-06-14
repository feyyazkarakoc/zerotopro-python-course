
x = 5

result = 5 < x < 10
print(result) # False

# x'i böyle bir matematiksel ifade yerine and, or veya not operasatörünü kullanabiliriz 

# and 
# True, True => True 
# True, False => False

result = (x > 5) and (x < 10)
print(result) # False

hak = 5
devam = "e"
result = (hak  > 0) and (devam == "e")
print(result) # True 

# or
# True, False => True 
# True, True => True 
# False, False => False 

result = (x > 0) or (x % 2 == 0)
print(result)  # True 

# not

x = 5

result = (x > 0)
print(result) # True 

result = not (x > 0)
print(result) # False

# x, 5 - 10 arasında olan bir çift sayı mı?

x = 8
result = ((x > 5) and (x < 10)) and (x % 2 == 0)
print(result) # True
