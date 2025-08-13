#– Ler um valor numérico inteiro qualquer e fazer a sua apresentação caso o valor seja maior que três, Utilize apenas o operador lógico not para a solução deste problema
valor = int(input("Digite um valor inteiro: "))
if not (valor <= 3):
    print(f"O valor {valor} é maior que três.")
else:
    print(f"O valor {valor} não é maior que três.")
    