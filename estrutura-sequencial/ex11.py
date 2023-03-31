"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: 
a- o produto do dobro do primeiro com metade do segundo .
b- a soma do triplo do primeiro com o terceiro.
c- o terceiro elevado ao cubo. 
"""

#Nota do desenvovedor: os números reais (R) contém os inteiros (Z), portanto o número 1 é real e inteiro: R ⊃ N. Acredito que o exercícios queira que o terceiro número seja um racional com decimais (Q).

num1 = int(input('Digite um número inteiro:'))
num2 = int(input('Digite mais um número inteiro:'))
num3 = float(input('Agora, digite um número racional com decimais.'))

a = (num1 * 2) * (num2 / 2)
b = (num1 * 3) + num3
c = num3 ** 3

print(f'O produto do dobro do primeiro, {num1 * 2}, com metade do segundo, {num2 / 2}, é igual a {a}.')
print(f'A soma do triplo do primeiro, {num1 * 3}, com o terceiro, {num3}, é igual a {b}.')
print(f'O terceiro, {num3}, elevado ao cubo é igual a {c}.')
