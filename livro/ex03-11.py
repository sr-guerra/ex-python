#Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
#Exiba o valor do desconto e o preço a pagar."""

preco_inicial =  float(input("Qual o valor da mercadoria?"))
desconto = float(input("Qual o percentual de desconto?"))

desconto = preco_inicial * desconto / 100
preco_final = preco_inicial - desconto

print(f"Foi descontado o valor de R${desconto:.2f}. O valor a pagar é R${preco_final:.2f}.")
