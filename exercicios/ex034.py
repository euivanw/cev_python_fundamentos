# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é o seu salário..: '))

if (salario > 1250.0):
    aumento = 0.10
else:
    aumento = 0.15

novo_salario = salario + (salario * aumento)
print('Seu novo salário é R$ {:.2f}'.format(novo_salario))
