# Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python.
# Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando módulos
# built-in e módulos externos, oferecidos no Pypi.
from math import ceil, sqrt, floor

numero = int(input('Digite um número.: '))
raiz = sqrt(numero)

print('A raiz quadrada de {} é {:.3f}.'.format(numero, raiz))
print('A raiz quadrada de {} é {}.'.format(numero, ceil(raiz)))
print('A raiz quadrada de {} é {}.'.format(numero, floor(raiz)))
