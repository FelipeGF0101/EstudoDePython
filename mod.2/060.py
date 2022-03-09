"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 
5! = 5 x4 x 3 x 2 x 1 = 120

# Forma simplificada

from math import factorial
num = int(input('Insira um valor: '))
f = factorial(num)
print(f'O fatorial de {num} é {f}.')
=============================================================
# Forma tradicional

num = int(input('Insira um valor: '))
cont = num
fat = 1
print(f'Calculando o fatorial de {num}! = ', end= '')
while cont > 0:
    print(f'{cont}', end= '')
    print(' X ' if cont > 1 else f' = {fat}', end= '')
    fat = fat * cont
    cont = cont - 1
"""
num = int(input('Digite um valor: '))
fat = 1
for i in range(num, 0, -1):
    fat = fat * i
print(f'O fatorial de {num}! é {fat}.')

