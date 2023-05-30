# Yöntem 1
# import math
# import math as islem    #takma isim koyabiliriz

# value = dir(math)
# value = help(math)
# value = help(math.factorial)
# value = math.sqrt(49)
# value = math.factorial(5)
# value = math.floor(5.9) #aşağı yuvarlama
# value = math.ceil(5.9)  #yukarı yuvarlama

# value = islem.factorial(5)



#Yöntem 2
# from math import * #tüm fonksiyonları alacaktır


from math import factorial,sqrt

def sqrt(x):    #aynı isimli olan fonksiyonlardan hangisi en son tanımlanırsa o kullanılır.Eğer başa alsaydık yine 3 bilgisi çıkacaktı.
    print('x : ' + str(x))

# value = factorial(5)
value = sqrt(9)
# value = ceil(5,8)   #ceil metodu tanımlanmadığı için çalışmayacaktır


print(value)