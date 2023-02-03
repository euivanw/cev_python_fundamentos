# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente deste ângulo.
import math

angulo = float(input('Digite o valor do ângulo..: '))

seno = math.sin(angulo)
coseno = math.cos(angulo)
tangente = math.tan(angulo)

print('Para o ângulo {}.'.format(angulo))
print('O seno é igual a {:.3f}.'.format(seno))
print('O coseno é igual a {:.3f}.'.format(coseno))
print('A tangente é igual a {:.3f}.'.format(tangente))
