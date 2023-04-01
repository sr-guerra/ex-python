#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. 

salh = int(input('Quantos reais você quanha por hora?'))
trah = int(input('Quantas horas por mês você trabalha?'))

resul = salh * trah

print(f'Se você quanha {salh} reais por hora e trabalha {trah} horas por mês, então seu salário é igual a {resul} reais mensais')
