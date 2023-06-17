#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. #Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:

# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

#Obs.: Salário Bruto - Descontos = Salário Líquido.

pagamento_hora = float(input("Quanto você ganha por hora?"))
horas_trabalhadas = float(input("Quantas horas você trabalhou neste mês?"))

salario_bruto = pagamento_hora * horas_trabalhadas
inss = (salario_bruto * 8 / 100)
sindicato = (salario_bruto * 5 / 100)
imposto_renda = (salario_bruto * 11 / 100)
salario_liquido = salario_bruto - inss - sindicato - imposto_renda

print(f"Salário bruto: R${salario_bruto:.2f};\nImposto de renda (11%): R${imposto_renda:.2f};\nINSS (8%): R${inss:.2f};\nSindicato(5%): R${sindicato:.2f};\nSalário líquido: R${salario_liquido:.2f}.")