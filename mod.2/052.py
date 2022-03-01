"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. 
"""
num = int(input('Digite um número: '))
tot = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[1;32m', end='')
        tot += 1  
    else:
        print('\033[1;31m', end='')
    print(f'{i}', end= ' ')

print(f'\nO número {num} foi dividido {tot} vezes.')
if tot == 2:
    print(f'O número {num} é um número primo.')
else:
    print(f'O número {num} não é primo')
    
