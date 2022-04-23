'''
Faça um programa que leia o nome e peso de várias pessoa, guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.

B) Uma listagem com as pessoas mais pesadas.

C) Uma listagem com as pessoas mais leves.

'''
pessoas = []
resp = ''
cont = 0
mais_pesado = 0
menos_pesado = 0


while resp != 'N':
    nome = str(input('Insira o nome: ')).capitalize()
    peso = int(input('Insira seu peso: '))
    cont += 1   
    resp = str(input('Deseja cadastrar mais alguém? [S/N]: ')).upper().strip()[0]
    dados = [nome, peso]
    pessoas.append(dados)
    if cont == 1:
        mais_pesado = menos_pesado = dados[1]
    else:
        if dados[1] > mais_pesado:
            mais_pesado = dados[1]
        if dados[1] < menos_pesado:
            menos_pesado = dados[1]

print(f'Ao todo, você cadastrou {cont} pessoas')
print(f'O maior peso foi de {mais_pesado} kg. Pertence à ', end='')
for p in pessoas:
    if p[1] == mais_pesado:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menos_pesado} kg. Pertence à ', end='')
for p in pessoas:
    if p[1] == menos_pesado:
        print(f'[{p[0]}]', end='')
