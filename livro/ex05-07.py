# Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada em vez de começar com 1 e 10.

print("Monte a sua tabuada.")
multiplicando = int(input("\nMultiplicando: "))
inicio = int(input("Multiplicador inicial: "))
fim = int(input("Multiplicador final: "))

while inicio <= fim:
    print(f"{multiplicando} x {inicio} = {multiplicando * inicio}")
    inicio = inicio + 1

