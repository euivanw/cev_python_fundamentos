# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por Km acima do limite.

velocidade = float(input('Digite a velocidade do carro.: '))

if (velocidade > 80.0):
    multa = (velocidade - 80.0) * 7
    print('Você ultrapassou a velocidade permitida.')
    print('O valor da multa é R$ {:.2f}.'.format(multa))
