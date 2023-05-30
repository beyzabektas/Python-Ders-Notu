# def changeName(n):
#     n = 'beyza'

# name = 'nur'
# changeName(name)
# print(name)


# def change(n):
#     n[0] = 'istanbul'

# sehirler = ['ankara','istanbul']
# n = sehirler[:]             #slicing
# n[0] = 'istanbul'

# change(sehirler[:])
# print(n)

# def add(a,b,c= 0):          #c parametresine değer atayarak hem 2 hem de  3 parametre kullanarak fonksiyonu çağırabiliriz.
#     return sum((a,b,c))

# print(add(10,20))
# print(add(10,20,30))

# def add(*params):
#     print(params)          
#     return sum((params))
# print(add(10,20))
# print(add(10,20,30,60,70,100))


# def add(*params):
#     print(type(params))
#     sum = 0          
#     for n in params:
#         sum += n
#     return sum
# print(add(10,20))
# print(add(10,20,30,60,70,100))

# def displayUser(**args):
#     print(type(args))
#     for key,value in args.items():
#         print('{} is {}'.format(key,value))
# displayUser(name = 'Beyza',age=24,city = 'Kocaeli')
# displayUser(name = 'Nur',age=22,city = 'İstanbul',phone = '123')


def myfunc(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myfunc(10,20,30,40,50,key1 = 'value 1',key2 = 'value 2')