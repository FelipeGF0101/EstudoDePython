"""
Crie um algoritmo que leia um número e mostre o seu dobro, o triplo e a raiz quadrada.

"""

print('Digite um número: ')
num=int(input())

dobro = num * 2

triplo = num * 3

raiz = num**(1/2)

print(f'O número escolhido foi {num}. Após a realização do cálculo, descobrimos que dobro do valor é {dobro} e', end=' ')
print(f'o triplo é {triplo}. Descobrimos também que a raiz é {raiz :.3f}.')

print('================================================================')

# Outra forma de fazer

n=int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(n,(n*2)))
print('O triplo de {} vale {}.'.format(n(n*3)))
print('A raiz quadrada de {} é igual a {:.2f}'.format(pow(n, (1/2))))
