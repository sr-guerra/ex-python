#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.

#Opção de codar sem módulos.

from math import hypot

cateto_oposto = float(input("Digite o comprimento do cateto oposto:"))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente:"))

hipotenusa = ((cateto_oposto ** 2) + (cateto_adjacente ** 2)) ** (1/2)

print(f"O comprimento da hipotenusa é {hipotenusa:.2f}.")

#Opção de codar com módulo.

cateto_oposto = float(input("Digite o comprimento do cateto oposto:"))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente:"))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f"O comprimento da hipotenusa é {hipotenusa:.2f}")
