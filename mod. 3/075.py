'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre: 
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.

'''

'''
RESOLUÇÃO DO GUANABARA

num = (int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')))

print(f'Você digitou os valores {num}')
'''
lista = []
for n in range(4):
    n = int(input('Digite um valor: '))
    lista.append(n)

tupla = (tuple(lista))
print(tupla)
if tupla.count(9) == 1:
    print(f'Existe {tupla.count(9)} número 9')
else:
    print(f'Existem {tupla.count(9)} números 9')
    
if 3 in tupla:
    print(f'O número 3 encontra-se na {tupla.index(3)}ª posição')
else:
    print('Não existe número 3 nesta lista!')

for n in tupla:
    if n % 2 == 0:
        print(f'O {n} é par.')
