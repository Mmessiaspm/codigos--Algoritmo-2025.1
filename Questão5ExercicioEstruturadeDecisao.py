#programa que Ler quatro valores numéricos inteiros e apresentar os valores que são divisíveis por 2 e 3.
a=int(input("Digite o primeiro valor: "))
b=int(input("Digite o segundo valor: "))
c=int(input("Digite o terceiro valor: "))
d=int(input("Digite o quarto valor: "))
if a % 2 == 0 and a % 3 == 0:
    print(f"{a} é divisível por 2 e 3")
else:
    print(f"{a} não é divisível por 2 e 3")
if b % 2 == 0 and b % 3 == 0:
    print(f"{b} é divisível por 2 e 3")
else:   
    print(f"{b} não é divisível por 2 e 3") 
if c % 2 == 0 and c % 3 == 0:
    print(f"{c} é divisível por 2 e 3")
else:   
    print(f"{c} não é divisível por 2 e 3")
if d % 2 == 0 and d % 3 == 0:
    print(f"{d} é divisível por 2 e 3")
else:   
    print(f"{d} não é divisível por 2 e 3")
#Fim do programa
