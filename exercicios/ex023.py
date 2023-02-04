# Faça um programa que leia um número a 0 e 9999 e mostre na tela cada um dos dígitos separado
# Ex:
#  Digite um número: 1834
#  Unidades: 4
#  Dezenas: 3
#  Centenas: 8
#  Milhares: 1

numero = input('Digite um número entre 0 e 9999.: ')
numero = numero.zfill(4)

print('Unidades: {}'.format(numero[3]))
print('Dezenas.: {}'.format(numero[2]))
print('Centenas: {}'.format(numero[1]))
print('Milhares: {}'.format(numero[0]))

numero = int(numero)

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('Unidades: {}'.format(unidade))
print('Dezenas.: {}'.format(dezena))
print('Centenas: {}'.format(centena))
print('Milhares: {}'.format(milhar))
