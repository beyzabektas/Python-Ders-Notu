names = ['Ali','Yağmur','Hakan', 'Deniz']
years = [1998,2000,1998,1987]

#1- "Cenk" ismini listenin sonunda ekleyiniz.
# names.append('Cenk')


#2- "Sena" değerini listenin başına ekleyiniz.
# names.insert(0,'Sena')


#3- "Deniz" ismini listeden siliniz.
# names.remove('Deniz')

#4- "Deniz" isminin indeksi nedir?
# index = names.index('Deniz') 
# print(index)
# names.pop(index)

#5- "Ali" listenin bir elemanı mıdır?
# result = 'Ali' in names
# print(result)

#6- Liste elemanlarını ters çevirin.
# names.reverse()

#7- Liste elemanlarını alfabetik olarak sıralayınız.
# names.sort()

# print(names)

#8- years listesini rakamsal büyüklüğe göre sıralayınız.
# years.sort()

# print(years)

#9- str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
# list = ['Chevrolet','Dacia']
# print(list)

#ya da

# str = "Chevrolet,Dacia" 
# print(str.split(','))

#10- years dizisinin en büyük ve en küçük elemanı nedir?
# min = min(years)
# max = max(years)
# print(min,max)

#11- years dizisinde kaç tane 1998 değeri vardır?
# print(years.count(1998))

#12- years dizisinin tüm elemanlarını siliniz.
# years.clear()
# print(years)

#13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
markalar = []
marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)