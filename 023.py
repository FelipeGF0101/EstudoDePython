"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""
numero = (input('Digite um número: '))


print(f"Unidade: {numero[3]}")
print(f"Dezena: {numero[2]}")
print(f"Centena: {numero[1]}")
print(f"Milhar: {numero[0]}")

# No formato acima, se eu digitar um número com menos de 4 dígitos, o programa retornará erro. Esse problema poderia ser resolvido com uma estrutura de repetição.

# Outra forma de fazer

num = int(input('Informe um número: '))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10

print(f"Unidade: {uni}")
print(f"Dezena: {dez}")
print(f"Centena: {cen}")
print(f"Milhar: {mil}")