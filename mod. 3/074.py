'''
Crie um programa que vai gerar cinco números aleatórios e coloca em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

'''
import random

lista = random.sample(range(0, 30), 5)
tupla = (tuple(lista))

print(f'Os valores gerados foram {tupla}. O maior valor é {max(tupla)} e o menor valor é {min(tupla)}.')
