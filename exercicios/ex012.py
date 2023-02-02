# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto.: R$ '))

desconto = preco * 5 / 100
preco_com_desconto = preco - desconto

print('Preço com desconto........: R$ {:.2f}'.format(preco_com_desconto))
