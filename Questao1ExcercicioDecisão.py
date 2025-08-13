#ler quatros notas de um aluno e verifica media
#se a media for maior ou igual a 7, aprovado
#se a media for menor que 7, reprovado
nota1= float(input('Digite a primeira nota: '))
nota2= float(input('Digite a segunda nota: '))
nota3= float(input('Digite a terceira nota: '))
nota4= float(input('Digite a quarta nota: '))
media= (nota1 + nota2 + nota3 + nota4) / 4
if media >= 7:
    print(f'Média: {media:.1f} - Aprovado')
else:
    print(f'Média: {media:.1f} - Reprovado')