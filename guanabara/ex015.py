#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

km = float(input("Quantos quilômetros você percorreu com o carro?"))

dia = float(input("Por quantos dias o carro foi alugado?"))

preco_fim = (km * 0.15) + (dia * 60)

print(f"O preço a pagar é R${preco_fim}.")
