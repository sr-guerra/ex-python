#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

saldo = float(input('Quantos reais você tem em sua carteira?'))

dolar = saldo / 3.27

print(f'Com R${saldo} em sua carteira, você pode comprar U${dolar:.2f} dolares.')
