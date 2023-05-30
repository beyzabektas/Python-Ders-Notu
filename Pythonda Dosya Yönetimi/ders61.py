# with open("newfile.txt","r+",encoding = "utf-8") as file:   #r+ modu hem açmak hem dosyayı okuma hem yazma modunu ifade eder.
#     file.seek(20)   #20.bytedan sonra denemeyi yazar.
#     file.write("deneme")

# with open("newfile.txt","r+",encoding = "utf-8") as file:
#     print(file.read())



#**************Sayfa sonunda güncelleme **********************
# with open("newfile.txt","a",encoding = "utf-8") as file:
#     file.write("\nselamke")


#**************Sayfa başında güncelleme **********************

# with open("newfile.txt","r+",encoding = "utf-8") as file:
#     content = file.read()
#     content = "canım\n" + content
#     file.seek(0)
#     file.write(content)
#     print(content)

with open("newfile.txt","r",encoding = "utf-8") as file:
    print(file.read())


#**************Sayfa ortasında güncelleme **********************

with open("newfile.txt","r+",encoding = "utf-8") as file:
    list = file.readlines()
    list.insert(1,"42kocaeli")  #contenti 1. indexten önce ekler.
    # help(list.insert)
    file.seek(0)
    file.writelines(list)
    # for i in list:
    #     file.write(i)

with open("newfile.txt","r",encoding = "utf-8") as file:
    print(file.read())