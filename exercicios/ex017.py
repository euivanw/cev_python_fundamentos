# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hiputenusa.
from math import hypot

cateto_oposto = float(input('Digite o comprimento do cateto oposto....: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente.: '))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print('A hipotenusa é igual a {:0.3f}.'.format(hipotenusa))
