x = 5

result = 5 < x < 10

#and

result = x > 5 and x < 10       #True,True => True

#or

result = x > 0 or x % 2 == 0    #True,False => True

#not

result = not(x > 0)             #True => False

#x, 5-10 arasında olan bir çift sayı mı?

result = (x>5) and (x<10) and (x%2 == 0)

print(result)