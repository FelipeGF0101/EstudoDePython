"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

""" 
print('Quantos reais você tem na carteira:R$', end=' ')
valor=float(input())
convert=valor/5.72

print(f'Com o valor de R$ {valor}, você consegue comprar USD$ {convert:.2f} dólares.')