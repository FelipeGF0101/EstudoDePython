"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

(existe uma regra pra isso)

"""
a = float(input('Digite o valor do lado A: '))
b = float(input('Digite o valor do lado B: '))
c = float(input('Digite o valor do lado C: '))

# Condição de existência de um triângulo: é preciso que quaisquer dois lados do triângulo sejam maiores que um terceiro lado.
if a + b > c and b + c > a and a + c > b:
    print('As medidas fornecidas PODEM FORMAR um triângulo!')
else:
    print('As medidas fornecidas NÃO PODEM FORMAR um triângulo!')