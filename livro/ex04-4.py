#Escreva um programa que pergunte o salário do funcionárioe calcule o valor do aumento.
#Para salários superores a R$1250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, de 15%.

salario = float(input("Digite qual o seu salário: R$"))

if salario > 1250.00:
    aumento = (salario * 10 / 100)
elif salario <= 1250.00:
    aumento = (salario * 15 / 100)

print(f"O senhor receberá um aumento de R${aumento:.2f}.")

