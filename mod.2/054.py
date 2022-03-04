"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

"""
from datetime import date
id1 = 0
id2 = 0
for idades in range(1, 8):
    num = int(input(f'Digite a {idades}ª data de nascimento: '))
    ano = date.today().year
    calc = ano - num
    if calc > 18:
        print(calc)
        print('Já é maior!')
        id1 = id1 + 1
    else:
        print(calc)
        print('Ainda é menor!')
        id2 = id2 + 1

print(f'O número de pessoas que já atingiram a maior idade é {id1} e o número de pessoas menores é {id2}.')