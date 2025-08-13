#Ler o nome e o sexo de uma pessoa e apresentar como saída uma das seguintes mensagens: “Ilmo. Sr.”, caso seja informado o sexo masculino, ou  “Ilma. Sra” ,caso seja informado o sexo feminino. Apresentar também junto de cada mensagem de saudação o nome previamente informado.
nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M/F) ou O se preferir não informar: ").strip().upper()
if sexo == 'M':
    print(f"Ilmo. Sr. {nome}")
elif sexo == 'F':
    print(f"Ilma. Sra. {nome}")
elif sexo == 'O':
    print(f"Ilmo. Sr./Ilma. Sra. {nome}")    
else:
    print("Sexo inválido. Por favor, informe 'M' para masculino ou 'F' para feminino.")