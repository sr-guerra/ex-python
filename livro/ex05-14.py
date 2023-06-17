# Escreva um programa que leia números inteiros do teclado.
# O programa deve ler os números até que o usuário digite 0(zero).
# No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

repeticao = 1
acumulador = 0

while True:
    numero = int(input("Digite um número inteiro para ser somado; 0 para finalizar o processo: "))

    if numero == 0:
        break

    acumulador += numero
    repeticao += 1

print(f"Quantidade de números digitados: {repeticao - 1};\nSoma dos números: {acumulador};\nMédia aritmética: {acumulador / (repeticao-1)}.")

