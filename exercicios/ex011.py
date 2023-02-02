# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m2.

largura = float(input("Informe a largura.: "))
altura = float(input("Informe a altura..: "))

area = largura * altura
tinta = area / 2

print('São necessários {:.1f} litros de tinta para pintar uma área de {:.1f} metros.'.format(tinta, area))
