#Escreva um programa que pergunte a velocidade do carro de um usuário.
#Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado.
#Nesse caso, exiba o valor da multa, cobrando R$5,00 por km acima de 80km/h.

velocidade = int(input("Qual a velocidade de seu carro? km/h: "))
if velocidade > 80:
    print(f"O senhor foi multado em R${(velocidade - 80) * 5:.2f}.")
else:
    print("O senhor não foi multado.")
