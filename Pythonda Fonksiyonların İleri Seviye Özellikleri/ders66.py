# def my_decorator(func):
#     def wrapper(name):
#         print("fonksiyondan önce işlemler")
#         func(name)
#         print("fonksiyondan sonraki işlemler")
#     return wrapper

# @my_decorator #sayHello'yu my decorator'e çağırarak aynı işlemi yapmış olduk.
# def sayHello(name): #eğer name adında parametre ekliyorsak bunu hepsinde kullanmamız gerekir.
#     print("hello",name)

# def sayGreeting():
#     print("greeting")

# sayHello = my_decorator(sayHello)
# sayGreeting = my_decorator(sayGreeting)
# sayHello('beyza')
# sayGreeting()

import math
import time

def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1)

        func(*args, **kwargs)

        finish = time.time()
        print("fonksiyon " + func.__name__ + str(finish-start) + " saniye sürdü.")
    return inner

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))
    
@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

@calculate_time
def toplama(a,b):
    print(a+b)


usalma(2,3)
faktoriyel(4)
toplama(10,20)