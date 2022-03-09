"""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci.

Ex: 0 > 1 > 1 > 2 > 3 > 5 > 8



"""
# FORMA COMUM
inicio = int(input('Quantos termos deseja mostrar? '))
tt1 = 0
tt2 = 1
cont1 = 3
print(f'{tt1} -> {tt2}', end='')
while cont1 <= inicio:
    tt3 = tt1 + tt2
    tt1 = tt2
    tt2 = tt3
    cont1 = cont1 + 1
    print(f' -> {tt3}', end='')
print('-> FIM')

# COM OPÇÃO DE MOSTRAR MAIS VALORES

n = int(input('Quantos termos deseja mostrar? '))
t1 = 0
t2 = 1
mais = n
total = 0
cont = 3 # Deve começar com 3 porque já conta o t1, t2 e o t3.
print(f'{t1} -> {t2}', end='')
while mais != 0:
    total = total + mais
    while cont <= total:
        t3 = t1 + t2
        t1 = t2 # T1 vai assumir o lugar de t2 na sequência
        t2 = t3 # T2 vai assumir o lugar de t3.
        cont = cont + 1
        print(f' -> {t3}',end='')
    print('-> FIM')
    mais = int(input('Quantos você deseja mostrar a mais? '))
print('-> FIM!')