#class

class Person:
    pass
    #class attributes
    adress = 'no information'

    #constructor(yapıcı metod)
    def __init__(self,name,year):
        #object attributes
        self.name = name
        self.year = year
        print('init metodu çalıştı.')
        #methods

#object,instance
p1 = Person(name = 'Beyza',year= 1999)
p2 = Person(name= 'Nur',year = 1998)

#updating
p1.name = 'Ahmet'
p2.adress = 'Kocaeli'

#accessing object atttributes
print(f'p1 name: {p1.name} year: {p1.year} adress : {p1.adress}')
print(f'p2 name: {p2.name} year: {p2.year} adress : {p2.adress}')

print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1 == p2)         #False
