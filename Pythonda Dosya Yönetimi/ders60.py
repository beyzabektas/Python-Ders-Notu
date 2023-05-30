with open("newfile.txt","r",encoding="utf-8") as file:  #with ile oluşturduğumuz kod bloğunun sonuna geldiğimiz zaman otomatik olarak kapanacak yani file.close() kullanmamıza gerek olmayacak.
    content =file.read()
    content =file.read(10)  #bu sefer ilk 10 tanesini okur.
    print(content)
    file.seek(0)    #içeriği en başa gönderir
    # file.seek(10)   #10'dan başlayarak yazdırır.
    print(file.tell())  #konumunu verir
    content2 = file.read()  #yaptığımızda bir bilgi vermez çünkü kodun sonu tell fonksiyonuna gelmektedir.
    print(content2)
