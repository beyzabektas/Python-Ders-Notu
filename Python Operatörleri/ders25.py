#Identity Operator : is

# x = y = [1,2,3]
# z = [1,2,3]
# print(x == y)
# print(x == z)
# print(x is y)
# print(x is z)       #x ve z'nin aynı adresi tutup tutmadığı önemlidir.Bu yüzden False çıkacaktır.

# x = [1,2,3]
# y = [2,4]
# del x[2]
# y[1] = 1
# y.reverse()
# print(x == y)
# print(x is y)          #Objeler aynı olsa da farklı adresleri gösterdikleri için yine False çıakcaktır.
# print(x is not y)

#Membership Operator : in

x = ['apple', 'banana']
print('banana' in x)    #True

name = 'Çınar'
print('a' in name)
print('a' not in name)  #False