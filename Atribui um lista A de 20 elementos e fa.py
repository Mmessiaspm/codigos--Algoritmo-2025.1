#Atribui um lista A de 20 elementos e fazer com que uma lista B seja os elementos de A em ordem decrescente.

a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
b=[]
for i in range(len(a)-1,-1,-1):
    b.append(a[i])
print(b)
