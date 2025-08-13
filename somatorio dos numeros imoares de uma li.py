#somatorio dos numeros imoares de uma lista A
a=[1,2,3,4,5]
soma = 0
for i in range(0, len(a)):
    if a[i] % 2 != 0:
        soma+=a[i]
print(soma)



        
        