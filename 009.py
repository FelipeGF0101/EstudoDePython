"""
Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

"""
cont = 0

print('Digite um valor: ')
valor=int(input())
while cont < 10:
    cont=cont+1
    result=valor*cont
    print(f'{valor} X {cont:2} = {result}') # Esse trecho serve para organizar os números em duas casas decimais



    