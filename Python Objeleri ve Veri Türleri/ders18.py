#value types => string,number
x = 5
y = 25

x = y
y = 10

# print(x,y)

#reference types => list,class

a = ["apple","banana"]
b = ["apple","banana"]

a = b           #yaptığımızda ikisi de aynı adresi taşıyor olduğundan yaptığımız değişiklikler ikisine de uygulanacaktır.
b[0] = "grape"
print(a,b)
