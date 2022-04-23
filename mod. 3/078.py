'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor 
valor digitado e as suas respectivas posições na lista.

'''
valores = []
mai = 0
men = 0
for i in range(0, 5):
    num = int(input('Insira um valor: '))
    valores.append(num)
    if i == 0:
        mai = men = valores[i]
    else: 
        if valores[i] > mai:
            mai = valores[i]
        if valores[i] < men:
            men = valores[i]

print(f'Você digitou os valores {valores}.')
print(f'O maior valor digitado foi {mai} nas posições -> ', end= '')
for e, v in enumerate(valores):
    if v == mai:
        print(f'{e}...', end='')
print()
print(f'O menor valor digitado foi {men} nas posições -> ', end= '')
for e, v in enumerate(valores):
    if v == men:
        print(f'{e}...', end='')
print()
