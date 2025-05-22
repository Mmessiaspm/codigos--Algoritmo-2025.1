#Calcula o salario liquido de um professor
hora_aula = 50
hora_trabalhada = int(input("Quantas horas o professor trabalhou? "))
salario_bruto = hora_aula * hora_trabalhada

#calculo do desconto do inss
desconto_inss = salario_bruto * 0.15

#calculando o salario liquido
salario_liquido = salario_bruto - desconto_inss
print("O Salário liquido é:", salario_liquido)

