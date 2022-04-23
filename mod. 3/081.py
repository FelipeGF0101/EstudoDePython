'''
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenados de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista
'''
valores = []
resp = ''
while resp != 'N':
    num = int(input('Digite um valor: '))
    valores.append(num)
    resp = input('Deseja continuar? [S/N]: ').upper()

if 5 not in valores:
    print('O valor 5 não foi digitado!')
else: 
    print('O valor 5 já consta na lista!')

valores.sort(reverse=True)
print(f'Foram digitados {len(valores)} valores. Em ordem descrescente, são eles: {valores}.')