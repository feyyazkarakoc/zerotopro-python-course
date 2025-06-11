
message = "Hello There. My name is Sadık Turan.".split()
print(message) # ['Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan.']
print(message[0]) # Hello

my_list = [1, 2, 3]
print(my_list) # [1, 2, 3]

my_list = ["bir", 2, True, 5.6]
print(my_list) # ['bir', 2, True, 5.6]

list1 = ["one", "two", "three"]
list2 = ["four", "five", "six"]

numbers = list1 + list2
print(numbers) # ['one', 'two', 'three', 'four', 'five', 'six']
print(len(numbers)) # 6
print(numbers[3]) # four

userA = ["Sadık", 36]
userB = ["Çınar", 2]

users = userA + userB
print(users) # ['Sadık', 36, 'Çınar', 2]

users = [userA, userB]
print(users) # [['Sadık', 36], ['Çınar', 2]]
print(users[1]) # ['Çınar', 2]
print(users[1][0]) # Çınar