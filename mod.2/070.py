"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
(cadastrar nome do produto e preço)
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.
"""
soma = cont = 0 
cont1 = 0 

while True:
    nome = str(input('\033[1;32mInsira o nome do produto:\033[m '))
    print('<=>=<=>' * 5)
    prec = float(input('\033[1;32mInsira o preço do produto:R$\033[m '))
    soma = soma + prec

    if prec > 1000:
        cont = cont + 1
        if cont > 1:
            prod = 'produtos custam'
        else:
            prod = 'produto custa'
    else:
        prod = ' produtos vendidos por'

    cont1 = cont1 + 1
    if cont1 == 1 or prec < menor:
        menor = prec
        menor1 = nome
    
    print('<=>=<=>' * 5)
    resposta = str(input('\033[1;31mDeseja continuar cadastrando produtos? [S/N]\033[m ')).upper().strip()[0]

    while resposta != 'S' and resposta != 'N':
        print('RESPONDA APENAS COM "S" OU "N"!')
        resposta = str(input('\033[1;31mDeseja continuar cadastrando produtos? [S/N]\033[m ')).upper().strip()[0]
    print('<=>=<=>' * 5)
    if resposta == 'N':
        break

print(f'\033[1;32mO valor total gasto na compra foi de R$ {soma:.2f}. Um total de {cont} {prod} mais de R$ 1000. O produto mais barato é {menor1}, custando apenas R$ {menor:.2f}!\033[m')
