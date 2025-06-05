
# Liste metotları

numbers = [1, 10, 5, 16, 4, 9, 10]

letters = ["a", "g", "s", "b", "y", "a", "s"]

val = min(numbers)
print(val) # 1

val = max(numbers)
print(val) # 16

val = min(letters)
print(val) # a

val = max(letters)
print(val) # y

val = numbers[3 : 6]
print(val) # [16, 4, 9]

val = numbers[: 3]
print(val) # [1, 10, 5]

val = numbers[4 : ]
print(val) # [4, 9, 10]

numbers[4] = 40
print(numbers) # [1, 10, 5, 16, 40, 9, 10]

numbers.append(49)
print(numbers) # [1, 10, 5, 16, 40, 9, 10, 49]

numbers.append(59)
print(numbers) # [1, 10, 5, 16, 40, 9, 10, 49, 59]

numbers.insert(3 , 78) # Dikkat!!! verdiğimiz index numarasından önceye ekler. Kendine yer açar, bir sağa kaydırır.
print(numbers) # [1, 10, 5, 78, 16, 40, 9, 10, 49, 59]

numbers.insert(-1, 52)
print(numbers) # [1, 10, 5, 78, 16, 40, 9, 10, 49, 52, 59] Dikkat!!! verdiğimiz index numarasından önceye ekler.
# Kendine yer açar, bir sağa kaydırır.

numbers.pop() # En son elemanı siler.
print(numbers) # [1, 10, 5, 78, 16, 40, 9, 10, 49, 52]

numbers.pop(0) # pop'a index verebiliriz
print(numbers) # [10, 5, 78, 16, 40, 9, 10, 49, 52]

# pop() ile pop(-1) aynı
numbers.pop(-1)
print(numbers) # [10, 5, 78, 16, 40, 9, 10, 49]

# Silmek istediğimiz rakamı remove metoduna verebiliriz
numbers.remove(78)
print(numbers) # [10, 5, 16, 40, 9, 10, 49]

numbers.sort()
print(numbers) # [5, 9, 10, 10, 16, 40, 49]
numbers.reverse()
print(numbers) # [49, 40, 16, 10, 10, 9, 5]

print(letters) # ['a', 'g', 's', 'b', 'y', 'a', 's']
letters.sort()
print(letters) # ['a', 'a', 'b', 'g', 's', 's', 'y']
letters.reverse()
print(letters) # ['y', 's', 's', 'g', 'b', 'a', 'a']

print(len(numbers)) # 7
print(len(letters)) # 7

print(numbers.count(10)) # 2
print(letters.count("a")) # 2

numbers.clear()
print(numbers) # []