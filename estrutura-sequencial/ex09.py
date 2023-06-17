#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius C = 5 * ((F-32) / 9).

f = float(input('Digite uma temperatura em fahrenheit:'))
c = 5 * ((f - 32) / 9)

print(f'{f} graus fahrenheit é igual a {c:.1f} graus celsius.')
