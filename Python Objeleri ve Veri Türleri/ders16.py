'''
ogrenciler = {'120':{'ad':'Beyza','soyad':'Bektaş','telefon': '539 463'},
              '125':{'ad':'Sultan','soyad':'Kaya','telefon':'533 555'},
              '128': {'ad':'rojda','soyad':'arapoglu','telefon':'532 614'}}
'''
#1-Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilere dictionary içinde saklayınız.

ogrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

# ogrenciler[number] = {'ad':name,'soyad':surname,'telefon':phone}
#  ya da
ogrenciler.update({number: {'ad':name,'soyad':surname,'telefon':phone}})

# print(ogrenciler)


# 2-Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.

print('*' * 50)
ogrNo = input('öğrenci no: ')
ogrenci =ogrenciler[ogrNo]
print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı:{ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}")

