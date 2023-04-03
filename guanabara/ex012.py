#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preço = float(input('Qual o preço do produto?'))

dcon = preço*5/100

final = preço - dcon

print(f'Com um desconto de 5% você pagará {final} reais.')
