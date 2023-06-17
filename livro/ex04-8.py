#Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
#Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/).
#Exiba o resultado da operação solicitada.

operacao = input("Qual operação matemática você deseja realizar: adição, subtração, multiplicação ou divisão? ");

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

adicao = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

if operacao == "adição": print(adicao)
elif operacao == "subtração": print(subtracao)
elif operacao == "multiplicação": print(multiplicacao)
elif operacao == "divisão": print(divisao)
        