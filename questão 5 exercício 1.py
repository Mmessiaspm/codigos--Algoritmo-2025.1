#questão 5 exercício 1
tempo_gasto=float(input("Digite o tempo gasto na viagem em horas: "))
velocidade_media=float(input("Digite a velocidade média em km/h: "))
distancia_percorrida=tempo_gasto*velocidade_media
litros_usados=distancia_percorrida/12
print("A velocidade média é: ",velocidade_media)
print("O tempo gasto na viagem é: ",tempo_gasto)
print("A distância percorrida na viagem é: ",distancia_percorrida)
print("A quantidade de litros de combustível gastos na viagem é: ",litros_usados)

