s = "diego.es10@yopmail.com"
print (s.split('@'))
if(s.split('@')[1] == "yopmail.com"):
    print("este correo no es valido")
else:
    print("Bienvenido")

name = "Fred"
print("bienvenido de nuevo {}".format(name))

list = [1,2,5,3,2,10,0,24,6]
print(list)
list.sort()
print(list)

#Test

a = 'hello'
print(a[::-1])
print(a[4])
print(a[-1])

list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'good bye'
print (list3)

list4 = [5,3,4,6,1]
print(list4)
print(list4[-2])

