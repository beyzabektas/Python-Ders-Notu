fruits = {'orange','apple','banana'}

# print(fruits)
#print(fruits[0])       #indexlenemez

# for x in fruits:
#     print(x)

fruits.add('cherry')
fruits.update(['mango','grape'])    #rastgele elemanlar eklenir
fruits.remove('mango')
fruits.discard('apple')
fruits.pop()        #son eleman yerine herhangi bir elemanın silinmesi gerçekleşebilir.
fruits.clear()
print(fruits)

# myList = [1,2,5,4,4,2,1]
# print(set(myList))        #aynı olan sayılar çıkarılır.