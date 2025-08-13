#atribuir duas listas de 15 elmentos A e B e Unir as duas listas em uma terceira lista C
# e imprimir a lista C
a= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
b= [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
c=[]
for i in range(len(a)):
    c.append(a[i])
for i in range(len(b)):
    c.append(b[i])
print(c)