"""
Crie um programa que leia dois valores e mostre um menu na tela:
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""
import time
num1 = float(input('INSIRA O PRIMEIRO VALOR: '))
print('=-=-=-=-=' * 5)
num2 = float(input('INSIRA O SEGUNDO VALOR: '))
print('=-=-=-=-=' * 5)
print('CARREGANDO OPÇÕES...')
time.sleep(2)
op = 0
while op != 5:
    print('''
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    print('=-=-=-=-=' * 5)
    op = int(input('Qual é a sua opção? '))
    if op == 1:
        soma = num1 + num2
        print(f'O resultado da soma entre {num1} e {num2} é {soma}.')
    elif op == 2:
        mult = num1 * num2
        print(f'O resultado da multiplicação entre {num1} e {num2} é {mult}.')
    elif op == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'O maior número é {maior}')
    elif op == 4:
        print('Insira novos valores!')
        num1 = float(input('INSIRA O PRIMEIRO VALOR: '))
        num2 = float(input('INSIRA O SEGUNDO VALOR: '))
    elif op == 5:
        print('ENCERRANDO PROGRAMA! TENHA UM BOM DIA!')
    else:
        print('Opção inválida! Tente novamente.')
