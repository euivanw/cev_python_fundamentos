# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite seu salário R$: '))

aumento = salario * 15 / 100
novo_salario = salario + aumento

print('Seu novo salário é R$: {}'.format(novo_salario))
