"""Faça um programa em que você pode preencher com seu nome e ele lhe retorne uma mensagem."""

print('Por favor, informe o seu nome: ')
nome=input()

print(f'É um prazer te conhecer, {nome}!')

# outra forma

nome1=input('Informe seu nome: ')

print('É um prazer te conhecer {}!'.format(nome1))