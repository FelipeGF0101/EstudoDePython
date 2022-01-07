"""
Faça um programa que leia a largura e a altura de uma parede em  metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

"""
print('Informe a largura da parede: ')
largura=float(input())

print('Informe a altura da parede: ')
altura=float(input())

medida= largura*altura
tinta=medida/2

print(f'Sua parede tem dimensões correspondentes a {largura} de largura e {altura} de altura, resultando numa superficie de {medida}m².')

print(f'Serão necessários {tinta} litros de tinta.')

