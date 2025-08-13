#atribuir uma lista a de 15 elementos e calcular o somatório de cada elemento de a em b
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
b = []
for i in range(len(a)):
    soma=0
    for j in range(a[i]+1):
        soma += j
    b.append(soma)
print(b)