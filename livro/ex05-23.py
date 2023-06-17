# Escreva um programa que leia um número e verifique se é ou não um número primo.
# Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o número lido.
# Se o resto de uma dessas divisões for igual a zero, o número não é primo.
# Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.

numero = int(input("Digite um número: "))

if numero == 2:
    print("Primo.")

elif numero % 2 == 0:
    print("Não primo.")
    
else:
    impar = 3

    while impar <= numero:
        if impar == numero:
            print("Primo")
            break
            
        elif numero % impar == 0:
            print("Não primo.")
            
        impar+=2

    
    
