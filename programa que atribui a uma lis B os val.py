#programa que atribui a uma lis B os valores de uma lista A, de acorod com a seguinte regra
# se o valor for par, multiplica por 5, se impar, soma 5
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
for i in range(0, len(a)):
    if i % 2 == 0:
        b.append(a[i] * 5)
    else:
        b.append(a[i] + 5)
print(a)
print(b)
