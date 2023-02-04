# Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome.

nome = input('Digite um nome completo.: ').strip()

print('O nome da pessoa contém SILVA? R: {}'.format('SILVA' in nome.upper()))
