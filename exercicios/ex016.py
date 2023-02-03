# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex:
#    Digite um número: 6.127
#    O número 6.1274 tem a parte inteira 6.
from math import trunc

numero = float(input('Digite um número.: '))
inteiro = trunc(numero)

print('A parte inteira do número {} é igual a {}.'.format(numero, inteiro))
print('A parte inteira do número {} é igual a {}.'.format(numero, int(numero)))
