list = [1,2,3]

tuple = (1, 'iki', 3)

# print(type(list))
# print(type(tuple))

# print(list[2])
# print(tuple[2])

# print(len(list))
# print(len(tuple))

list = ['ali','veli']       #burada herhangi bir liste elemanının içini değiştirmiyoruz list'e tamamen farklı bir içerik ekliyoruz.
tuple = ('damla','ayşe','ayşe')
names =('demet','emel','ayşe') + tuple

list[0] = 'ahmet'
# tuple[0] = 'deniz'          #tuple'da herhangi bir eleman atandıktan sonra değiştiremiyoruz.Fakat toptan bir işlem yapılabiliyor.

print(tuple.count('ayşe'))
print(tuple.index('ayşe'))      #ayşenin ilk nerde varolduğunu yazar.

print(list)
print(tuple)
print(names)