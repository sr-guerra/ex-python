# Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair.
# Imprima a tabuada da operação escolida.
# Repita até que a opção saída seja escolhida.

while True:

    i = 1;
    tabuada = str(input("\nAdição;\nSubtração;\nMultiplicação;\nDivisão.\n\nescolha a tabuada: "))

    if tabuada == 'adição' or tabuada == 'Adição':

        numero = int(input("\nDigite um número: "))
        while i <= 10:
            print(f"{numero} + {i} = {numero + i}")
            i+= 1

    elif tabuada == 'subtração' or tabuada == 'Subtração':

        numero = int(input("\nDigite um número: "))
        while i <= 10:
            print(f"{numero} - {i} = {numero - i}")
            i+= 1
    
    elif tabuada == 'multiplicação' or tabuada == 'Multiplicação':

        numero = int(input("\nDigite um número: "))
        while i <= 10:
            print(f"{numero} x {i} = {numero * i}")
            i+= 1

    elif tabuada == 'divisão' or tabuada == 'Divisão':

        numero = int(input("\nDigite um número: "))
        while i <= 10:
            print(f"{numero} / {i} = {numero / i}")
            i+= 1
        
        