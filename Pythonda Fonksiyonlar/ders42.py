#1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.
# def yazdir(kelime,adet):
#     print(kelime * adet)

# yazdir('Merhaba\n',5)

#2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon yazın.
# def listeyeCevir(*params):
#     liste = []
#     for param in params:
#         liste.append(param)

#     return liste
# result = listeyeCevir(10,20,30,'Merhaba')
# print(result)

#3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
# sayi1 = int(input('sayı 1: '))
# sayi2 = int(input('sayı 2: '))

# def asalSayilariBul(sayi1,sayi2):
#     for sayi in range(sayi1,sayi2+1):
#         if sayi > 1:
#             for i in range(2,sayi):
#                 if sayi % i == 0:
#                     break
#             else:
#                 print(sayi)

# asalSayilariBul(sayi1,sayi2)


#4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürün.

def tamBolenleriBul(sayi):
    tamBolenleri = []
    for i in range(2,sayi+1):
        if sayi % i == 0:
            tamBolenleri.append(i)
    return tamBolenleri

print(tamBolenleriBul(20))
