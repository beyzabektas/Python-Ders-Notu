#1- Girilen 2 sayıdan hangisi byüktür?
# a = int(input('1.sayi: '))
# b = int(input('2.sayi: '))

# result = (a > b)
# print(f'a: {a} b: {b} den büyüktür : {result}')

#2- Kullanıcıdan 2 vize(%60) br final(%40) notunu alıp ortalama hesaplayınız.
# Eger ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# vize1 = int(input('1.vize: '))
# vize2 =int(input('2.vize: '))
# final = int(input('final: '))

# ortalama = ((vize1 + vize2)/2 * 0.6) + (final * 0.4)
# print(f'not ortalamanız: {ortalama} ve dersten geçme duurmunuz: {ortalama >= 50}')

#3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.
# a = int(input('sayi: '))
# sayi = (a % 2 == 0)
# print(f'girilen sayi: {a} çift olma durumu: {sayi}')

#4- Girilen sayının negatif pozitif durumunu yazdırın.
# a = int(input('sayi: '))
# sayi = (a > 0)
# print(f'girilen sayi: {a} pozitif olma durumu: {sayi}')

#5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
# (email: email@sadikturan.com parola:abc123)
email = 'email@sadikturan.com'
password = 'abc123'

girilenEmail = input('email: ')
girilenPassword = input('parola: ')

isEmail = (email == girilenEmail.lower().strip())
isPassword = (password == girilenPassword)
print(f'Email bilgisi doğru mu: {isEmail} ve Parola doğru mu: {isPassword}')