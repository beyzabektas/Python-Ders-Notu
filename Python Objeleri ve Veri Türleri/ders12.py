numbers = [1,10,5,16,4,9,10]
letters = ['a', 'g' , 's' ,'b', 'y', 'a' , 's']

# val = min(numbers)
# val = max(numbers)
# val = min(letters)
# val = max(letters)

# val = numbers[3:6]
# val = numbers[:3]
# val = numbers[4:]
# print(val)

# numbers[4] = 40
# print(numbers)

# numbers.append(59)
# numbers.insert(3,78)    # 3. indexten sonra 78 ekler
# numbers.insert(-1,52)
# numbers.pop()           # son elemanı siler içine yazdığımız indexi silmek için de kullanabiliriz
# numbers.remove(59)
# print(numbers)

numbers.sort()            # küçükten büyüğe sıralar
letters .sort()
numbers.reverse()         # tersine sıralar
letters.reverse()
print(numbers)
print(letters)
print(len(numbers))
print(numbers.count(10))    # kaç tane 10 olduğunu sayar

numbers.clear()
print(numbers)