# Imprima de 1 até o número digitado pelo usuário, mas, dessa vez, apenas os números ímpares.

fim = int(input("Digite o último número a imprimir: "))
x = 0

while x <= fim:
    if x % 2 != 0:
        print(x)
    x = x + 1