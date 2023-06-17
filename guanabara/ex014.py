#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input("Digite uma temperatura em graus Celsius:"))

fahren = (celsius * 9/  5) + 32

print(f"{celsius}ºC é igual a {fahren}ºF")
