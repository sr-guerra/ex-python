#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58 

h = float(input('Qual a sua altura? '))

p_ideal = (72.7 * h) - 58

print(f'Seu peso ideal é {p_ideal:.3f}kg.')
