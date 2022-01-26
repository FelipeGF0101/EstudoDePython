"""
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

"""
from datetime import date # Importação da biblioteca e da funcionalidae date

ano = int(input('Informe um ano: '))
if ano == 0: # Se o programa receber o valor zero, ele irá entender que para usar a data atual registrada no computador.
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é um ano BISSEXTO!')
else: 
    print(f'O ano de {ano} NÃO é um ano BISSEXTO!')

