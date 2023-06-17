#Escreva um programa que leia três números e imprima o maior e o menor.

num1 = float(input("Digite um número: "))
num2 = float(input("Digite mais um número: "))
num3 = float(input("Digite novamente um número: "))

if num1 > num2 and num1 > num3: print(f"O maior número é {num1}.")
elif num2 > num1 and num2 > num3: print(f"O maior número é {num2}.")
elif num3 > num1 and num3 > num2: print(f"O maior número é {num3}.")

if num1 < num2 and num1 < num3: print(f"O menor número é {num1}.")
elif num2 < num1 and num2 < num3: print(f"O menor número é {num2}.")
elif num3 < num1 and num3 < num2: print(f"O menor número é {num3}.")
