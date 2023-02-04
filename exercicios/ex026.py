# Faça um programa que leia uma frase pelo teclado e mostre:
#  - Quantas vezes aparece a letra A
#  - Em que posição ela aparece na primeira vez
#  - Em que posição ela aparece na última vez

frase = input('Digite uma frase.: ')

print('Quantidade de As: {}'.format(frase.upper().count('A')))
print('Primeira posição que o A aparece: {}'.format(frase.upper().find('A')))
print('Última posição que o A aparece: {}'.format(frase.upper().rfind('A')))
