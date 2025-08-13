#atribui uma lista a e b e atribui a uma lista c o valor de a - b
a=[1,2,3,4,5,6,7,8,9,10]
b=[5,7,15,9,25,11,35,13,45,15]
c=[]                                
for i in range(len(a)):
    c.append(a[i]-b[i])
print(a)
print(b)
print(c)

