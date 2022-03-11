"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles. (Desconsiderando o flag).

"""
soma = 0
cont = 0
while True:
    n = int(input('Insira um valor (use 999 para parar): '))
    if n == 999:
        break
    cont = cont + 1
    soma = soma + n
print('FIM')
print(f'Você digitou {cont} valores. A soma deles foi {soma}.')