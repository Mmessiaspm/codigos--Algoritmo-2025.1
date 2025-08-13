#soma dos números de 1 a 100 utilixando while
soma = 0
i = 1
while i <= 500:  # Alterado para somar até 500
    if i % 2 == 0:  # Somente números pares
        soma += i
    i += 1
print(f'A soma dos números pares de 1 a 500 é: {soma}')