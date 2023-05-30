liste = ["1","2","5a", "10b","abc","10","50"]

#1- Liste elemanları içindeki sayısal değerleri bulunuz.

# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue

#2- Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayısal olduğundan emin olunuz aksi halde hata mesaj yazın.

# while True:
#     sayi = input('sayı: ')
#     if sayi == 'q':
#         break
#     try:
#         result = float(sayi)
#         print('girdiğiniz sayı ',result)
#         break
#     except:
#         print('geçersiz sayı')
#         continue

#3- Girilen parola içinde türkçe karakter hatası veriniz.

# def checkPassword(parola):
#     turkce_karakterler = 'şŞÇçğüöıİÖ'

#     for i in parola:
#         if i in turkce_karakterler:
#             raise TypeError('parola türkçe karakter içermemelidir.')
#         else:
#             pass
#     print('geçerli parola')

# parola = input('parola: ')

# try:
#     checkPassword(parola)
# except TypeError as er:
#     print(er)

#4- Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajlar verin.

def faktöriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError('negatif değer')
    result = 1
    for i in range(1,x+1):  #range de son x parametresi işin içine katılmaz ama x + 1 dediğimizde katmış oluruz.
        result *= i

    return result

for x in [5,10,20,-3,'10a']:
    try:
        y = faktöriyel(x)
    except ValueError as er:
        print(er)
        continue
    print(y)