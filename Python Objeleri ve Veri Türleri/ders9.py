website = 'www.sadikturan.com'
course = "Python Kursu: Baştan Sona Python Porgramlama Rehberiniz (40 saat)"

#1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
# result = ' Hello World '.strip()
# result = ' Hello World '.rstrip()    # sadece sağ tarafı silmek isteseydik
# result = ' Hello World '.lstrip()    # sadece sol tarafı silmek isteseydik

#2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
# result=website[4:14]
# result = 'www.sadikturan.com'.strip('w.moc')

#3- 'course' karakter dizisinin tüm karakterini küçük harf yapın.
# result = course.lower()

#4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
# result = website.count('a')

#5- 'website' 'wwww' ile başlayıp com ile bitiyor mu?
# result = website.startswith('www')
# result = website.endswith('com')

#6- 'website' içinde '.com' ifadesi var mı?
# result = website.find('.com',0,10)       #bu aralıkta kelime yoksa -1 değeri döndürür
# result= course.find('Python')
# result= course.rfind('Python')

#7- 'course' içindeki karakterlerin hepsi alfabetik mi ? (isalpha,isdigit)
# result = course.isalpha()
# result = 'Hello'.isalpha()
# result = '1234'.isdigit()

#8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
# result ='Contents'.center(50,'*')
# result ='Contents'.ljust(50,'*')      #sadece sola * ekler
# result ='Contents'.rjust(50,'*')      #sadece sağa * ekler

#9 - 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
# result = course.replace(' ','-')

#10 - 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
# result = 'Hello World'.replace('World','There')

#11 - 'course' karakter dizisinin boşluk karakterlerinden ayırın
result = course.split(' ')
print(result)