"""
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

"""

from math import trunc # Função trunc recebe um float e retorna um int, excluindo a parte decimal. 

num = float(input("Digite um número: "))
num1 = trunc(num)
print(f"A parte inteira do número é: {num1}")

"""
Poderia ser assim também:
# Importando a biblioteca completa.

import math

num = float(input('Digite um valor: '))

print('O valor digitado foi {} e a sua porção inteira é {}'.format(num,math.trunc(num)))

======================================================================================

Poderia ser assim também: 

# Resolve o problema sem a necessidade de importar uma biblioteca.

num = float(input('Digite um valor: '))

print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))

OU

num = float(input("Digite um valor: "))

print(f"O valor digitado foi {num} e sua parte inteira é {format(int(num))}")

"""
