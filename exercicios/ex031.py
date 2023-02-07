# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens até 200Km e R$ 0,45 para viagens mais longas.

distancia = float(input('Digite a distância da viagem em Km: '))

if (distancia <= 200.0):
    passagem = distancia * 0.5
else:
    passagem = distancia * 0.45

print('Preço da passagem R$ {:.2f}.'.format(passagem))

passagem = distancia * 0.5 if distancia <= 200.0 else distancia * 0.45

print('Preço da passagem R$ {:.2f} (simplificado).'.format(passagem))
