"""
Crie um programa que leia vários números pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
soma = 0
maior = 0
menor = 0
cont = 0
resposta = 'S'
while resposta != 'N':
    num = int(input('Digite um valor: '))
    soma = soma + num
    cont = cont + 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Deseja continuar? ')).upper().strip()[0]
print('FIM')
print(f'A soma de todos os valores digitados é {soma}. A média dos valores é {soma/cont:.2f}.')
print(f'O maior valor é {maior} e o menor é {menor}.')