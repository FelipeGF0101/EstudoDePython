"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag (o 999)).
"""
print('Digite os valores. Caso não queima mais continuar, basta digitar [999]')
num = int(input('Digite o valor: '))
cont = 0
soma = 0
while num != 999:
    cont = cont + 1
    soma = soma + num
    num = int(input('Digite o valor: '))
print('FIM')
print(f'A quantidade de números digitados foi {cont} e a soma de todos os valores foi {soma}!')
