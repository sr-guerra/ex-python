"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

    a- Para homens: (72.7*h) - 58
    b- Para mulheres: (62.1*h) - 44.7 
"""
s = input('Você é homem ou mulher?')
h = float(input('Digite a sua altura:'))

a = (72.7 * h) - 58
b = (62.1 * h) - 44.7

if s == 'homem':
    print(f'Seu peso ideal é {a}.')

if s == 'mulher':
    print(f'Seu peso idel é {b}.')