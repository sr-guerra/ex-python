#Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que R$1200,00.

salario = float(input('Qual é o seu salário: R$'))

if salario >= 1200:
    print('Você deve pagar imposto.')
else: 
    print('Você não deve pagar imposto.')
