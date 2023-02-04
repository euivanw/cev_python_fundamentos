# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último número
# separadamente.
#
#  Ex: Ana Maria de Souza
#  primeiro = Ana
#  ultimo - Souza

nome = input('Digite um nome completo.: ').strip()
nome_separado = nome.split()

print('Primeiro nome.: {}'.format(nome_separado[0]))
print('Sobrenome.....: {}'.format(nome_separado[len(nome_separado) - 1]))
