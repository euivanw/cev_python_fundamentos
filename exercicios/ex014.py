# Escreva um programa que converta uma temperatuva digitada em graus celcius e converta para graus fahrenheit

temperatura = float(input('Digite a temperatura em °C.: '))
conversao = ((temperatura * 9) / 5) + 32

print('A temperatura de {:.1f}°C é igual a {:.1f}°F.'.format(temperatura, conversao))
