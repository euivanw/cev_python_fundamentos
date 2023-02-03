# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente deste ângulo.
from math import sin, cos, tan, radians

angulo = float(input('Digite o valor do ângulo..: '))

radianos = radians(angulo)
seno = sin(radianos)
coseno = cos(radianos)
tangente = tan(radianos)

print('Para o ângulo {} e em radianos {:.2f}.'.format(angulo, radianos))
print('O seno é igual a {:.2f}.'.format(seno))
print('O coseno é igual a {:.2f}.'.format(coseno))
print('A tangente é igual a {:.2f}.'.format(tangente))
