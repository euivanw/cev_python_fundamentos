# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro número..: '))
n2 = int(input('Digite o segundo número...: '))
n3 = int(input('Digite o terceiro número..: '))

menor = n1
maior = n1

if n2 < menor:
    menor = n2
if n2 > maior:
    maior = n2
if n3 < menor:
    menor = n3
if n3 > maior:
    maior = n3

print('Resultado:')
print('Menor.: {}.'.format(menor))
print('Maior.: {}.'.format(maior))
