# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Digite a quantidade de km percorridos..: '))
dias = int(input('Digite a quantidade de dias de aluguel.: '))

valor_km = km * 0.15
valor_aluguel = dias * 60
valor_total = valor_km + valor_aluguel

print('Você terá que pagar R$ {:0.2f} pelo aluguel do carro.'.format(valor_total))
