"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos. 

"""
peso1 = []
for peso in range(1, 6):
    num = float(input(f'Digite seu peso, pessoa {peso}: '))
    peso1.append(num)

print(f'O maior peso foi {(max(peso1))}. O menor peso foi {(min(peso1))}.')

# OUTRA FORMA DE FAZER
# maior = 0
# menor = 0
# for p in range(1, 6):
#   peso = float(input('Peso da {}ª pessoa: '.format(p)))
#   if p == 1:
#       maior = peso
#       menor = peso
#   else:
#       if peso > maior:
#           maior = peso
#       if peso < menor:
#           menor = peso
#
# print('O maior peso lido foi de {}Kg'.format(maior))
# print('O menor peso lido foi de {}Kg'.format(menor))