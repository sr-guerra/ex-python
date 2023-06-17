# Escreva um programa que leia dois números.
# Imprima a multiplicação do primeiro pelo segundo.
# Utilize apenas os operadores de soma e subreação para calcular o resultado.
# Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles.
# Assim, 4 x 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

num1 = float(input("digite o multiplicando: "))
num2 = float(input("Digite o multiplicador: "))
resultado = 0

while num2 != 0:
    resultado = resultado + num1
    num2 = num2 - 1

print(resultado)
