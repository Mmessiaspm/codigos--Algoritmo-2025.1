#de celsius para fahrenheit de 10 em 10 graus utilizando while
#https://pt.stackoverflow.com/q/58688/101
celsius = 10
while celsius <= 100:
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} graus Celsius é igual a {fahrenheit} graus Fahrenheit.")
    celsius += 10