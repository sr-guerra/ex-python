#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra:")
vogal = ["a", "e", "i", "o", "u"]
consoante = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

if letra in vogal:
    print("O senhor digitou uma vogal.")
elif letra in consoante:
    print("O senhor digitou uma consoante.")
else:
    print("Uma letra não foi digitada.")