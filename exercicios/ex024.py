# Crie um programa que leia o nome de uma cidade e digita se ela começa ou não com o nome 'Santo'

cidade = input('Digite o nome de uma cidade.: ').strip()

print('O nome da cidade começa com Santo? R: {}'.format(cidade.upper().startswith('SANTO')))
