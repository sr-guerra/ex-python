#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
#Calcule o total em segundos.

dias = int(input("Digite os seus dias:"))
horas = int(input("Digite as suas horas:"))
minutos = int(input("Digite os seus minutos:"))
segundos = int(input("Digite os seus segundos:"))

minutos = minutos * 60
horas = horas * 3600
dias = dias * 86400

segundos = segundos + minutos + horas + dias

print(f"O total em segundos é igual a {segundos}.")
