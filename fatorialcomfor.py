#programa que calcula o fatorial de um numero
# com o for

numero = int(input("Digite um numero: "))
fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i
print(f"O fatorial é: {fatorial}")



