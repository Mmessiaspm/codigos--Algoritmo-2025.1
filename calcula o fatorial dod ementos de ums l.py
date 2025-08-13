#calcula o fatorial dod ementos de ums lista A e atribui a uma lista b
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
for i in a:
    fatorial = 1
    for j in range(1, i + 1):
        fatorial *= j
    b.append(fatorial)
print(a)
print(b)
