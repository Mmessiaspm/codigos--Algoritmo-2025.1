#tabuada de multiplicar def um numero qualquer utilizando while
numero = int(input('Digite um numero: '))
print(f'Tabuada do {numero}:')
contador = 1
while contador <= 10:
    print(f'{numero} x {contador} = {numero * contador}')
    contador += 1