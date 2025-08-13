#calcularo fatorial de n numeros lidos utilizando o while e calcula o somatorio dos fatoriais com while
count= 1
somatorio = 0
while count <= 5:
    n = int(input("Digite um número inteiro positivo: "))
    #calcular o fatorial de n
    fatorial = 1
    i = 1
    while i <= n:
        fatorial *= i
        i += 1
    somatorio += fatorial
    count += 1
print(f"A soma dos fatoriais é: {somatorio}")
