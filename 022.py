"""
Crie um programa que leia o nome completo de uma pessoa e mostre:

> O nome com todas as letras maiúsculas

> O nome com todas as letras minúsculas

> Quantas letras ao todo (sem considerar espaços)

> Quantas letras tem o primeiro nome.

"""

nome = input('Digite seu nome completo:\n ')
print('==============================')
print(f'Seu nome em letras maiúsculas:\n {nome.upper()}')
print('==============================')
print(f'Seu nome em letras minúsculas:\n {nome.lower()}')
print('==============================')
print(f'Seu nome tem ao todo:\n {len(nome.replace(" ",""))} letras.') # Tambem poderia ser: (len(nome) - nome.count(' '))
print('==============================')
print(f'Seu primeiro nome tem:\n {len(nome.split()[0])} letras') # Tambem poderia ser: (nome.find(' '))


