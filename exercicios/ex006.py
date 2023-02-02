# Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e a raiz quadrada.

numero = int(input('Digite um número inteiro: '))

print(f'Número digitado: {numero}')
print(f'Dobro: {numero * 2}')
print(f'Triplo: {numero * 3}')
print('Raiz Quadrada: {:0.2f}'.format(numero ** (1 / 2)))
print('Raiz Quadrada: {:0.2f}'.format(pow(numero, 1 / 2)))
