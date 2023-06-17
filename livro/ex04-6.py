#Escreva um programa que pergunte a distância que um pasageiro deseja percorre em km.
#Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até de 200 km, e R$0,45 para viagens mais longas.

distancia = float(input("Qual a distância por você desejada a percorrer em km?"))

if distancia <= 200:
    print(f"A passagem custará R${distancia * 0.50:.2f}.")
else:
    print(f"A passagem custará R${distancia * 0.45:.2f}.")
