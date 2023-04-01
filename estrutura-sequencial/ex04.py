#Faça um Programa que peça as 4 notas bimestrais e mostre a média. 

nota1 = int(input('Qual o valor da nota do primeiro bimestre?'))
nota2 = int(input('Qual o valor da nota do segundo bimestre?'))
nota3 = int(input('Qual o valor da nota do terceiro bimestre?'))
nota4 = int(input('Qual o valor da nota do quarto bimestre?'))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'A média de suas quatro notas bimestrais é igual a {media}.')
