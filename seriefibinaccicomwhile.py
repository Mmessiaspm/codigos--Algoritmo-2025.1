#quinze primeiro elementos da serie de fobonacci com while sem utilizar listas
a, b = 1, 1
count = 1
while count <= 15:
    print(f"{count}º: {a}")
    aux = a
    a = b
    b = aux + b
    count += 1