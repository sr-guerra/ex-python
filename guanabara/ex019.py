"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido."""

from random import choice

aluno1 = input("Qual o nome do primeiro aluno?")
aluno2 = input("Qual o nome do segundo aluno?")
aluno3 = input("Qual o nome do terceiro aluno?")
aluno4 = input("Qual o nome do quarto aluno?")

alunos = [aluno1, aluno2, aluno3, aluno4]

print(f"O aluno sorteado foi {choice(alunos)}.")
