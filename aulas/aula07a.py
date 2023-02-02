# Operadores Aritméticos:
#   +  Adição
#   -  Subtração
#   *  Multiplicação
#   /  Divisão
#   ** Potência ou pow(a, b)
#   // Divisão inteira
#   %  Resto da divisão
#   == Testar se duas coisas são iguais
#
# Ordem de Precedência:
#   1 ()       Parênteses
#   2 **       Exponenciação
#   3 * / // % Multiplicação, Divisão, Divisão Inteira ou Resto da Divisão
#   4 + -      Soma e Substração
#

nome = input('Qual é seu nome: ')
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:_^20}!'.format(nome), end='\n\n')
