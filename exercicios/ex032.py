# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = int(input('Digite um ano.: '))
eh_divisivel_por_4 = ano % 4
eh_divisivel_por_100 = ano % 100
eh_divisivel_por_400 = ano % 400


if eh_divisivel_por_4 == 0 and eh_divisivel_por_100 != 0 and eh_divisivel_por_400 != 0:
    print('O ano {} é bissexto'.format(ano))
