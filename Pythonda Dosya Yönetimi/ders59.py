# try:
#     file = open("newfile2.txt","r")  #ikinci parametre vermemiş olsak bile varsayılan olarak "r" atanır.
# except FileNotFoundError:
#     print("dosya okuma hatası")
# finally:
#     print("dosya kapandı.")
#     file.close()


file = open("newfile.txt","r",encoding= "utf-8")

###################for döngüsü###################
# for i in file:
#     print(i,end = "")   #end koymasaydık boşluk koymadan bilgilerimiz yeni satırda ekrana gelirdi.



###################read fonksiyonu###################
# content = file.read()
# print("içerik 1")
# print(content)
# file = open("newfile.txt","r",encoding= "utf-8")    #bu satır eklenmeseydi içerik 2 boş algılanacaktı.
# content2 = file.read()
# print("içerik 2")
# print(content2)
# file.close()

# content = file.read(5)
# content = file.read(3)  #ilk 5 karakterden sonraki 3 karakteri alır.
# print(content)
# file.close()

###################readline() fonksiyonu ###################

# print(file.readline(),end = "")
# print(file.readline(),end = "")
# print(file.readline(),end = "")
# file.close()


###################readlines() fonksiyonu ###################

liste = file.readlines()    #her bir satır bilgiyi bir dizi elemanı olarak alır.
print(liste)
print(liste[0])
print(liste[1])
print(liste[2])
file.close()