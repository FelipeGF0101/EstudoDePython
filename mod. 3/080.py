'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final mostre, a lista ordenada na tela.

'''
valores = []
num1 = 0
for i in range(0, 5):
    num = int(input('Digite um valor: '))
    if num > num1:
        num1 = num
        valores.append(num)
    if num < num1:
        valores.insert(0,num)

print(valores)