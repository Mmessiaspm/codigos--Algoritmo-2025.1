#programa que calcula o fatorial de um numero qualquer com while
numero = int(input("Digite um numero inteiro positivo: "))
fatorial = 1    
while numero > 1:
    fatorial *= numero
    numero -= 1
print(f"O fatorial é: {fatorial}")

