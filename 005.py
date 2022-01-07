"""
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

"""
print('Digite um número: ')
n1=int(input())
n=n1-1

print(f'O número antecessor de {n1} é {n}.')
n2=n1+1
print(f'O número sucessor de {n1} é {n2}.')

print("==========================================")
# Forma simplificada

n=int(input('Digite um número: '))
a=n-1
s=n+1

print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n,a,s))

print("===========================================")
# Forma mais simplificada. Utilizando apenas uma variável

n=int(input('Digite um número:'))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n,(n-1), (n+1)))