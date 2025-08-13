#Ler três valores e apresenta-los em ordem crescente. Utilizar os conceitos de propriedade distributiva e troca de valores entre variáveis.
#https://pt.stackoverflow.com/q/272682/101
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))    
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print(f'Os valores em ordem crescente são: {a}, {b} e {c}.')
#https://pt.stackoverflow.com/q/272682/101
