# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$ 1,00 = R$ 3,27

dinheiro = float(input('Digite quanto dinheiro você tem.: '))

print('Reais    R$.: {:10.2f}'.format(dinheiro))
print('Dólares US$.: {:10.2f}'.format(dinheiro * 3.27))
