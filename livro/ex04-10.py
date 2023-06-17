# Escreva um programa que calcule o preço a pagar oelo fornecimento de energia elétrica.
# Pergunte a quantidade de kWh consumida e o tipo de instalação:
# R para residências, I para indústrias e C para comércios.
# Calcule o preço a pagar de acordo com a tabela a seguir. 
"""
+---------------------------------------+
|   Preço por tipo e faixa de consumo   |
+---------------------------------------+
| Tipo        | Faixa (kWh)   | Preço   |
+=======================================+
| Residencial | Até 500       | R$ 0,40 |
|             | Acima de 500  | R$ 0,65 |
+---------------------------------------+
| Comercial   | Até 1000      | R$ 0,55 |
|             | Acima de 1000 | R$ 0,60 |
+---------------------------------------+
| Industrial  | Até 5000      | R$ 0,55 |
|             | Acima de 5000 | R$ 0,60 |
+---------------------------------------+
"""

kwh = float(input("Quantos quilowatts-hora (kWh) você consome?"))
instalacao = input('Qual o tipo de sua instalação?\n\n"R": residência;\n"I": indústria;\n"C": comécio.')
preco = 0

if instalacao == "R":
    if kwh <= 500:
        preco = 0.40
    else:
        preco = 0.65

elif instalacao == "C":
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.60

elif instalacao == "I":
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.60

else:
    print("Instalação inválida.")
    break

preco_pagar = kwh * preco

print(f"O preço a pagar é: R${preco_pagar:.2f}.")