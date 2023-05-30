#yield'de üretilen değer üretildiği anda kullanılarak bellek üzerinde yer kaplamıyor.
# def cube() :
#     result = []

#     for i in range(5):
#         yield i ** 3    

# for i in cube():
#     print(i)


# liste = [i**3 for i in range(5)]
generator = (i**3 for i in range(5))
print(generator)
# print(next(generator))

for i in generator:
    print(i)