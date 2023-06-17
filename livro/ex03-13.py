#Escreva um programa que converta uma temperatura digitada em Celsius para Fahrenheit.
#A Fórmula para essa conversão é: F = (9 * C / 5) + 32"""

celsius = float(input("Digite uma temperatura em graus Celsius:"))

fahrenheit = (9 * celsius / 5) + 32

print(f"{celsius}ºC equivale a {fahrenheit}ºF.")
