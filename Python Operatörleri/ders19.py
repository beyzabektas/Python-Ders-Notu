# x = 5
# y = 10
# z = 20

x,y,z = 16,10,20
# x,y = y,x 
x += 5          # x = x + 5
x -= 5
x *= 5
x /= 5
x %= 5
x //= 5         #bölümün yalnızca tam sayı kısmını alır ondalıklı kısma bakmaz.

y //= 5
y **= 5
# print(x,y,z)

values = 1,2,3,4,5

print(values)
print(type(values))

x,y,*z = values      #eleman daha az veya daha fazlaysa problem çıkartır.


print(x,y,z[0])