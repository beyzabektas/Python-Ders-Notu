website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Porgramlama Rehberiniz (40 saat)"
# 1- course karakter dizisinde kaç karakter bulunmaktadır?
result = len(course)
length = len(website)

# 2- website içinden wwww karakterilerini alın
result = website[7:10]

# 3- website içinden com karakterini alın
result=website[22:25]
result =website[length-3:length]

# 4- course içinden ilk 15 ve son 15 karakterlerini alın
result = course[:15]
result = course[-15:-1]

#5- course ifadesinin karakterini tersten yazdırın
result= course[::-1]
s = '12345' * 5        
# print(s)                 #12345 5 defa yan yana yazılacaktır
# print(s[::5])            #sadece 1'i 5 defa yazdıracaktır


#6- 'Benim adım Beyza Bektaş, Yaşım 24 ve mesleğim mühendis.'ifadeyi yazdır
name,surname,age,job = 'Beyza','Bektaş', 24, 'Mühendis'
result = "Benim adım " + name + " " + surname +", Yaşım " + str(age) + " ve mesleğim " + job
result = "Benim adım {} {},Yaşım {} ve mesleğim {}.".format(name,surname,age,job)   #yerlerini değiştirmek istersek {} içerisine index numaralarını yazmamız gerekir {0} gibi
result = f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}."

#7 - 'Hello world' ifadesindeki w harfini 'W' ile değiştirin
s = 'Hello world'
result = s[0:6] + 'W' + s[-4:]

#8 - 'abc' ifadesini yan yana 3 defa yazdır
result = 'abc ' * 3
print(result)