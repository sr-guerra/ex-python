#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. (0c x 9/5) + 32 = 32f

c = float(input('Digite uma temperatura em graus celsius:'))

f = 32 + (c * 9/5)

print(f'{c} graus celsius é igual a {f} graus fahrenheit.')
