"""O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada."""

from random import sample

aluno1 = input("Digite o nome do primeiro aluno:")
aluno2 = input("Digite o nome do segundo aluno:")
aluno3 = input("Digite o nome do terceiro aluno:")
aluno4 = input("Digite o nome do quarto aluno:")

alunos = [aluno1, aluno2, aluno3, aluno4]

print(f"A ordem de apresentação dos alunos será {sample(alunos, k=4)}.")
                            