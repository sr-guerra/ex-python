#Escreva uma expressão que será utilizada pra decidir se um aluno foi ou não aprovado, todas as médias do aluno devem ser maiores que 7.
#Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: matéria1, matéria2, matéria3.

materia1 = float(input('Qual foi a sua primeira nota:'))
materia2 = float(input('Qual foi a sua segunda nota:'))
materia3 = float(input('Qual foi a sua terceira nota:'))

media = (materia1 + materia2 + materia3) / 3 
if media > 7: 
    print(f'Sua média foi {media:.2f}. Você foi aprovado.')
else:
    print(f'Sua média foi {media:.2f}. Você não foi aprovado.')
    