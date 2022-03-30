'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 
        'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
        'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Insira um valor entre 0 e 20: '))
    if num > 20 or num < 0:
        print('Insira um número entre 0 e 20!')
    else:
        print(numeros[num].upper())
    resposta = input('Quer continuar? [S/N] ').upper().strip()
    if resposta == 'N':
        break
    
    