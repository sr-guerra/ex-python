#Faça um Programa que leia três números e mostre o maior deles.

num1 = float(input("Digite um número:"))
num2 = float(input("Digite mais um número:"))
num3 = float(input("Digite novamente um número:"))

if num1 > num2 and num1 > num3: print(f"O número {num1} é o maior.")
elif num2 > num1 and num2 > num3: print(f"O número {num2} é o maior.")
elif num3 > num1 and num3 > num2: print(f"O número {num3} é o maior.")