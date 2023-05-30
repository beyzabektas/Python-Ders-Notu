#fonksiyon

# def sayHello(name = 'user'):        #herhangi bir parametre yollanmazsa user girilir.
#     return 'Hello ' + name

# msg = sayHello('Beyza')
# print(msg)

# def total(num1,num2):
#     return num1 + num2
# result = total(10,20)
# print(result)

def yasHesapla(dogumYili):
    return 2023 - dogumYili

# ageBeyza = yasHesapla(1999)
# print(ageBeyza)

def emekliligeKacYilKaldi(dogumYili,isim):
    '''
    DOCSTRING: Doğum yılınıza göre emekliliğinize kaç yıl kaldı
    INPUT : Doğum yılı
    OUTPUT: Hesaplanan yıl bilgisi
    '''
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik >0:
        print(f'emekliliğinize {emeklilik} yıl kaldı')
    else:
        print('Zaten emekli oldunuz')

emekliligeKacYilKaldi(1999,'Beyza')

print(help(emekliligeKacYilKaldi))  #Burada yardım alabiliriz.

list = [1,2,3]
print(help(list.append))

