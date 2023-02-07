# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar
# um triângulo.

r1 = float(input('Digite o comprimento da primeira reta.: '))
r2 = float(input('Digite o comprimento da segunda reta..: '))
r3 = float(input('Digite o comprimento da terceura reta.: '))

valida_r1 = r1 < (r2 + r3)
valida_r2 = r2 < (r1 + r3)
valida_r3 = r3 < (r1 + r2)

if valida_r1 and valida_r2 and valida_r3:
    print('Estas retas podem formar um triângulo.')
else:
    print('Estas retas não podem formar um triângulo.')
