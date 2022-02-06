"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

> O primeiro valor é maior
> O segundo valor é maior
> Não existe valor maior, os dois são iguais.

"""
num = int(input('Informe um valor: '))
num1 = int(input('Informe outro valor: '))

if num > num1:
    print(f'O valor {num} é maior que o {num1}.')
elif num1 > num:
    print(f'O valor {num1} é maior que o {num}.')
elif num == num1:
    print(f'Não existe valor maior, os dois são iguais.')