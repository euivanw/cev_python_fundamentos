# \033[0;33;44m
#
# Style         Text Back   Cores
# 0 None        30   40     Branco
# 1 Bold        31   41     Vermelho
# 4 Underline   32   42     Verde
# 7 Negative    33   43     Amarelo
#               34   44     Azul
#               35   45     Roxo
#               36   46     Ciano
#               37   47     Cinza

print('{}  Teste  {}'.format('\033[0;30;41m', '\033[m'))
print('{}  Teste  {}'.format('\033[4;33;44m', '\033[m'))
print('{}  Teste  {}'.format('\033[1;35;43m', '\033[m'))
print('{}  Teste  {}'.format('\033[0;30;42m', '\033[m'))
print('{}  Teste  {}'.format('\033[m', '\033[m'))
print('{}  Teste  {}'.format('\033[7;30m', '\033[m'))
