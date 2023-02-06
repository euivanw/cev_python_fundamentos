n1 = float(input('Digite a primeira nova.: '))
n2 = float(input('Digite a segunda nova..: '))
m = (n1 + n2) / 2

print('A sua média foi {:.1f}.'.format(m))

if m >= 6.0:
    print('Sua média foi boa, parabéns!')
else:
    print('Sua média foi ruim, estude mais!')

print('PARABÉNS' if m >= 6.0 else 'ESTUDE MAIS!')
