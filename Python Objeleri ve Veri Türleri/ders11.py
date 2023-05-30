#1- "Bmw,Mercedes,Opel,Mazda" elemanlarına sahip bir liste oluşturunuz.
list = ['Bmw','Mercedes','Opel','Mazda']
# print(list)

#2- Liste kaç elemanlıdır?
# print(len(list))

#3- Listenin ilk ve son elemanı nedir?
# print(list[0],list[-1])

#4- Mazda değerini Toyota ile değiştirin
# list[-1] = 'Toyota'
# print(list)

#5- Mercesed listenin bir elemanı mıdır?
# result= 'Mercedes' in list
# print(result)

#6- Listenin -2 indeksindeki değer nedir?
# print(list[-2])

#7- Listenin ilk 3 elemanını alın
# print(list[:3])

#8- Listenin son 2 elemanı yerine 'Toyota' ve 'Reanult' değerlerini ekleyin.
# list[-2:] = ['Toyota','Renault']
# print(list)

#9 - Listenin üzerine 'Audi' ve 'Nissan' değerlerini ekleyin.
# result = list + ['Audi','Nissan']
# print(result)

#10 - Listenin son elemanını silin.
# del list[-1]
# print(list)
# print(list[:-1])

#11- Liste elemanlarını tersten yazdırınız.
# print(list[::-1])

#12- Aşağıdaki verileri bir liste içinde saklayınız.
# studentA : Sultan Kaya 2002, (90,60,90)
# studentB : Rojda Arapoğlu 2000, (90,80,90)
# studentC : Beyza Bektaş 1999, (90,100,90)

studentA = ['Sultan', 'Kaya',2002, [90,60,90]]
studentB = ['Rojda','Arapoğlu',2000, [90,80,90]]
studentC = ['Beyza', 'Bektaş', 1999, [90,100,90]]

#13- Liste elemanlarını ekrana yazdırınız.
result = studentA[0]
result = studentB[1]
result = studentC[3][1]
result = f"{studentA[0]} {studentA[1]} {2023-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"
print(result)