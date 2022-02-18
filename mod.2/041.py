"""
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:

> Até 9 anos: MIRIM
> Até 14 anos: Infantil
> Até 19 anos: Júnior
> Até 20 anos: Sênior
> Acima de 20: Master
"""
from datetime import date

atual = date.today().year
print('========== CONFEDERAÇÃO NACIONAL DE NATAÇÃO =========')
nome = input('Digite seu nome: ')
print('==========' * 5)
idade = int(input('Ano de nascimento: '))
print('==========' * 5)
calc = atual - idade
if calc <= 9:
    print(f'{nome}, você se classifica como MIRIM')
elif calc > 9 and calc <=14: 
    print(f'{nome}, você se classifica como INFANTIL')
elif calc > 14 and calc <= 19:
    print(f'{nome}, você se classifica como JÚNIOR')
elif calc > 19 and calc <= 20:
    print(f'{nome}, você se classifica como SÊNIOR')
elif calc > 20:
    print(f'{nome}, você se classifica como MASTER') 