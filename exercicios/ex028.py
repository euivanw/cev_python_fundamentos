# Escreva um programa que faça o computador pensar em número entre 0 e 5 peça ao usuário tentar descobrir qual foi o
# número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

numero = int(input('Digite um número entre 0 e 5.: '))
numero_sorteado = randint(0, 5)

print('Processando...')
sleep(2)

if (numero == numero_sorteado):
    print('Parabéns, você ganhou!')
else:
    print('Você perdeu, o número sorteado foi {}.'.format(numero_sorteado))
