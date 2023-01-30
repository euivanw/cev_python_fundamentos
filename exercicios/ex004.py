# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.

string = input('Digite algo: ')

print('Tipo primitivo: {}'.format(type(string)))
print('É alfabético: {}'.format(string.isalpha()))
print('É alfanumérico: {}'.format(string.isalnum()))
print('É numérico: {}'.format(string.isnumeric()))
print('É ASCII: {}'.format(string.isascii()))
print('É decimal: {}'.format(string.isdecimal()))
print('É um dígito: {}'.format(string.isdigit()))
print('É um identificador do Python: {}'.format(string.isidentifier()))
print('É um imprimível: {}'.format(string.isprintable()))
print('É um espaço: {}'.format(string.isspace()))
print('Está em caixa baixa: {}'.format(string.islower()))
print('Está em caixa alta: {}'.format(string.isupper()))
print('Está no formato de título: {}'.format(string.istitle()))
