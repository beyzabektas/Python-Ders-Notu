#Inheritance (Kalıtım): Miras alma

#Person => name,lastnname,age,eat(),run(),drink()
#Student(Person),Teacher(Person)

#Animal => Dog(),Cat()

class Person():
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        print('Person Created')

    def who_am_i(self):
        print('I am a person')
    
    def eat(self):
        print('I am eating')

class Student(Person):  #Student çağırdığımızda yine person objesinden nesne üreteceğimiz için çıktı aynı olur.
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.studentNumber=number
        print('Student Created')

    #override
    def who_am_i(self):
        print('I am a student')
    
    def sayHello(self):
        print('Hello I am a student')

class Teacher(Person):
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname)   #bunu da kullanabiliriz.
        self.branch = branch

    def who_am_i(self):
        print(f'I am a {self.branch} teacher')

p1 = Person('Beyza','Bektaş')
s1 = Student('Nur','Şahin',24)
t1 = Teacher('Simay','Aşko','Math')

t1.who_am_i()
print(p1.firstname + ' ' + p1.lastname)
print(s1.firstname + ' ' + s1.lastname + ' ' + str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()   #student içinde olmasa bile metoda ulaşabiliriz.Aynı isimde bir metod temel sınıftaki metodu ezer buna "override" denir.

p1.eat()
s1.eat()

s1.sayHello() #bunu sadece student üzerinden çağırabiliriz çünkü persona özgü bir metod değildir.