"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, deconsidere-o.

"""
soma = 0
import random
print('-=-=-=-=-=-= SOMANDO INTEIROS -=-=-=-=-=-=-=')
for num in random.sample(range(0, 20), 6):
    print(num, end=', ')
    if num % 2 == 0:
        soma = soma + num

print(f'\n{soma}')

'''
OUTRA FORMA 
soma = 0
cont = 0

for c in range(1,7):
    num = int(input(f'Digite o {c} valor: '))
    if num % 2 == 0
    soma += num
    cont += 1
print(f'Você informou {cont} números pares. A soma de todos os números pares é {soma}.)
'''