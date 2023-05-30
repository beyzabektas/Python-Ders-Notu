# error => hata

# error handling => hata yönetimi

# print(a) => NameError
# int('1a2') => ValueError
# print(10/0) => ZeroDivisionError
# print('denem'e) => SyntaxError
# Python da exception hierarchy ile karşılaşabileceğimiz hatalara bakabiliriz.

# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)

# except (ZeroDivisionError,ValueError) as e:   #gelen hatanın nerden geldiğini öğrenmek için e objesi tanımlayabiliriz
#     print('yanlış bilgi girdiniz')
#     print(e)


while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)

    except Exception as ex:
        print('yanlış bilgi girdiniz',ex)
    else:
        break
    finally:        #finally bloğu her durumda çalışır.
        print('try except sonlandı.')