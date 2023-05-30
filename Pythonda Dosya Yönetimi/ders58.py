#Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
#Kullanımı: open(dosya_Adi,dosya_erişme_modu)
#dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

#"w" (write) yazma modu.Dosyayı konumda oluşturur.

# result = open("newfile.txt", "w")
# file.close()

# file = open("C:/users/beyza/newfile.txt","w")
# file.close()

# file = open("newfile.txt", "w",encoding = 'utf-8')      #encoding ile türkçe karakteri alabiliriz.
# file.write("Beyza Bektaş")
# file.close()

####################################################

#"a" (append) ekleme.Dosya konumda yoksa oluşturur.

# file = open("newfile.txt", "a",encoding = 'utf-8')   #içinde bilgi varsa üzerine yazar. 
# file.write("\nBeyza Bektaş")
# file.write("Beyza Bektaş\n")
# file.close()

####################################################

#"x" (create) oluşturma. Dosya zaten varsa hata verir.

file = open("newfile2.txt", "x",encoding = 'utf-8')   #tekrar çalıştırmaya çalışırsak dosya zaten varolduğu için hata verir.

#"r" (read)okuma.Varsayılan dosya konumda yoksa hata verir.