#RANGE metodu

# for item in range(2,10,2):
#     print(item)
# print(list(range(2,10,2)))


#ENUMERATE metodu

# index = 0
# greeting  = 'Hello There'

# for index,letter in enumerate(greeting):
    # print(f'index. {index} letter: {letter}')
    # index += 1

# greeting  = 'Hello'
# for item in enumerate(greeting):
#     print(item)


#ZIP metodu

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']

print(list(zip(list1,list2)))

for item in zip(list1,list2):
    print(item)

for a,b in zip(list1,list2):
    print(a)                    #yalnızca ilk liste bilgileri ekrana gelecektir.
    