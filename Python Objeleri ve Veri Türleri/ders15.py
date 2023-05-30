#key - value
#41 => kocaeli

# sehirler = ['kocaeli','istanbul']
# plakalar = [41,34]

# print(plakalar[sehirler.index('kocaeli')])

#print(plakalar['kocaeli']) => 41
#print(plakalar['istanbul']) => 34

# plakalar = {'key':'value'}
# plakalar = {'kocaeli':41,'istanbul':34}
# print(plakalar['kocaeli'])
# print(plakalar['istanbul'])

# plakalar['ankara'] = 6      #yaptığımızda listeye eklenir.
# print(plakalar)

users = {'beyzabektas':{'age' :24,'roles':['admin','user'],'email':'bebektas@gmail.com','adress':'kocaeli','phone':539463},'rojdaarapoglu':{'age' :23,'email':'roarapog@gmail.com','adress':'kocaeli','phone':539111},'sultankaya':21}
print(users['beyzabektas'])
print(users['beyzabektas']['email'])
print(users['beyzabektas']['roles'])