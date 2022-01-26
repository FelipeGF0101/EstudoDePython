"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

"""
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))

menor = num1 # Aqui eu estou simplesmente escolhendo um elemento para usar como parâmetro para os outros dois. 
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

print(f'O menor valor digitado foi {menor}.')

maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print(f'O maior valor digitado foi {maior}.')