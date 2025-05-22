#Reajusta salário
salario=float(input("Digite o salário: "))
#calcuoando o reajuste do salario
if(salario<500):
    novo_salario=salario*1.15
else:
    if(salario<=1000):
        novo_salario=salario+1.10
    else:
        novo_salario=salario*1.05

print("Novo salário: R$%.2f" % novo_salario)

