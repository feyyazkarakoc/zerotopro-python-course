
a, b, c, d = 5, 5, 10, 4

result = (a == b) 
print(result) # True

result = (a == c)
print(result) # False

password = "1234"
username = "sadikturan"

result = ("sdktrn" == username)
print(result) # False

result = ("sadikturan" == username)
print(result) # True

result = (a != b)
print(result) # False

result = (a != c)
print(result) # True

result = (a > b)
print(result) # False

result = (a > c)
print(result) # False

result = (a < c)
print(result) # True

result = (a >= b)
print(result) # True

result = (c <= b)
print(result) # False

result = (True == 1)
print(result) # True

result = (False == 0)
print(result) # True

result = False + True + 40
print(result) # 41
