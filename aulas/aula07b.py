n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

soma = n1 + n2
subtracao = n1 - n2
divisao = n1 / n2
divisao_inteira = n1 // n2
resto = n1 % n2
exponenciacao = n1 ** n2
multiplica_string = 'Oi' * n2

print(f'A soma vale {soma}')
print(f'A subtração vale {subtracao}')
print('A divisão vale {:.2f}'.format(divisao))
print(f'A divisão inteira vale {divisao_inteira}')
print(f'Resto da divisão vale {resto}')
print(f'A exponenciação vale {exponenciacao}')
print(f'Multiplica a palavra [Oi]: {multiplica_string}')
