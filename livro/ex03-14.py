#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

distancia_percorrida = float(input("Qual foi a quilometragem percorrida por você?"))
dias_alugados = float(input("Por quantos dias o carro foi alugado?"))

preco_pagar = (distancia_percorrida * 0.15) + (dias_alugados * 60)

print(f"O preço a pagar é R${preco_pagar:.2f}.")
