# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quadro alunos e mostre a ordem sorteada.
import random

aluno1 = input('Digite o nome do primeiro aluno.: ')
aluno2 = input('Digite o nome do segundo aluno..: ')
aluno3 = input('Digite o nome do terceiro aluno.: ')
aluno4 = input('Digite o nome do quarto aluno...: ')

alunos = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.randint(0, 3)
aluno1 = alunos[sorteio]
alunos.remove(aluno1)

sorteio = random.randint(0, 2)
aluno2 = alunos[sorteio]
alunos.remove(aluno2)

sorteio = random.randint(0, 1)
aluno3 = alunos[sorteio]
alunos.remove(aluno3)

aluno4 = alunos[0]
print('A ordem do sorteio foiL {}, {}, {} e {}.'.format(aluno1, aluno2, aluno3, aluno4))
