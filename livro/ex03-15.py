#Escreva um programa para calcular a redução do tempo de vida de um fumante.
#Pergunte a quantidade cigarros fumados por dia e há quantos anos que ele fuma.
#Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. 
#Exiba o total em dias.

cigarros_dia = int(input("Quantos cigarros o senhor fuma por dia?"))
anos_fumo = int(input("Há quantos anos o senhor fuma?"))

vida_perdida_min = (cigarros_dia * 10) * (anos_fumo * 365)
vida_perdida_dia = vida_perdida_min / (24 * 60)

print(f"O senhor perdeu {vida_perdida_dia:.1f} dias de vida por conta do cigarro.")
