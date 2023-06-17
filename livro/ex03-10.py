#Faça um programa que calcule o aumento de um salário.
#Ele deve solicitar o valor do salário e a porcentagem do aumento.
#Exiba o valor do aumento e do novo salário.

salario = float(input("Qual o valor de seu salário?"))
aumento = float(input("Qual será o valor de aumento?"))

novo_salario = salario + (salario * aumento / 100)

print(f"O valor de seu novo salário é: R${novo_salario:.2f}.")
