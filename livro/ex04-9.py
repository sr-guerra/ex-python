#Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
#O programa deve perguntar o valor da casa a comprar, o salário e a quantidade anos a pagar.
#O valor da pretação mensal não pode ser superior a 30% do salário.
#Calcule o valor da pretação como sendo o valor da casa a comprar dividido pelo númeero de meses a pagar.

valor_casa = float(input("Digite o valor da casa a comprar: R$"))
salario = float(input("Digite o valor de seu salário: R$"))
anos_pagar = int(input("Digite a quantidade de anos a pagar: "))

prestacao = (valor_casa / (anos_pagar * 12))

if prestacao > (salario * 30 / 100): print("Empréstimo negado.")
else: print(f"Empréstimo concedido. Prestação a se pagar: R${prestacao:.2f}")
