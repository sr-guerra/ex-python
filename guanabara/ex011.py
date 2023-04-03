#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m quadrados.

b = float(input('Qual a largura da parede que você deseja pintar?'))
h = float(input('Qual a altura da parede que você deseja pintar?'))

a = b * h 

tinta = a / 2

print(f'Você precisará de {tinta}l de tinta para pintar uma parede de área {a}m.')
