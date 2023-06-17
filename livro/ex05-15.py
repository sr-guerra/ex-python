#Escreva um programa para controlar uma pequena máquina registradora.
#Vocẽ deve solicitar ao usuário que digite o código do produto e a quantidade comprada.
#Utilize a tabela de códigos a seguir para obter o preço de cada produto:

#1: 0,5;
#2: 1,00;
#3: 4,00;
#5: 7,00;
#9: 8,00;

#Seu programa deve exibir o total das compras depois que o usuário digitar "0".
#Qualquer outro código deve gerar a mensagem de erro "Código inválido".

total = 0

print("Para parar o programa e receber o(s) resultado(s), digite '0'.\n")

while True:

    quantidade = int(input("\nDigite a quantidade comprada: "))

    if quantidade == 0:
        break

    codigo = int(input("Digite o código do produto: "))

    if codigo == 1:
        total = total + (0.5 * quantidade)
    elif codigo == 2:
        total = total + (1 * quantidade)
    elif codigo == 3:
        total = total + (4 * quantidade)    
    elif codigo == 5:
        total = total + (7 * quantidade)
    elif codigo == 9:
        total = total + (8 * quantidade)
    elif codigo != 1 and codigo != 2 and codigo != 3 and codigo != 5 and codigo != 9:
        print("\nCódigo inválido.")

print(f"\nTotal das compras: R${total:.2f}.")
