#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input('Qual o seu salário?'))

aum = sal*15/100

fim = sal + aum

print(f'Seu novo salário será de {fim:.2f} reais.')
