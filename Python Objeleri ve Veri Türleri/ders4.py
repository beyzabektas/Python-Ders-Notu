pi = 3.14
r =float(input("yarı çap: "))
#inputtan girilen veri string
alan = pi * (r ** 2)
cevre = 2 * pi * r
print("alan: " + str(alan) + " çevre: " + str(cevre))
#bu şekilde float ve string ifadeleri birleştiremeyiz o yüzden ifadeyi str çevirmemiz gerek
