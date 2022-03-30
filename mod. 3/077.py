'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.
'''
lista = ('Felipe', 'Gustavo', 'Computador', 'Programação', 'vogais', 'otorrinolaringologia')

for item in lista:
    print(f'\nTemos na palavra {item.upper():.<30} ',end='')
    for letra in item:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')