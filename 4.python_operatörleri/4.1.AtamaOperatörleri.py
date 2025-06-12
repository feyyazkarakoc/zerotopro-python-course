
# x = 5
# y = 10
# z = 20

#ya da 
x, y, z = 5, 10, 20

print(x, y, z) # 5 10 20

x, y = y, x
print(x, y, z) # 10 5 20

x = x + 5 # x += 5
print(x) # 15

x -= 5 # x = x - 5
print(x) # 10

x *= 5 # x = x * 5
print(x) # 50

x /= 10 # x = x / 10
print(x) # 5.0

x %= 5 # x = x % 10
print(x) # 0.0

x, y, z = 5, 16, 20

y //= 3 # y = y // 3
print(y) # 5

y **= 5 # y = y ** 5
print(y) # 3125 

values = (1, 2, 3)
print(values, type(values)) # (1, 2, 3) <class 'tuple'>

x, y, z = values
print(x, y, z) # 1 2 3

# a, b = values
# print(a, b) # ValueError: too many values to unpack (expected 2)

# values = 1, 2
# a, b, c = values
# print(a, b, c) # ValueError: not enough values to unpack (expected 3, got 2)

values = 1, 2, 3, 4, 5
x, y, *z = values
print(x, y, z) # 1 2 [3, 4, 5]
print(z[0]) # 3


