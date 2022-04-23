'''
Crie um programa que vai ler vários número e colocar em uma lista.

Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.

'''
valores = []
valores_pares = []
valores_ímpares = []
resp = ''

while resp != 'N':
    num = int(input('Digite um valor: '))
    valores.append(num)
    resp = input('Deseja continuar? [S/N]: ').upper()
    if num % 2 == 0:
        valores_pares.append(num)
    else:
        valores_ímpares.append(num)

print(f'Todos os valores digitados foram {valores}')
print(f'Os valores pares são {valores_pares}')
print(f'Os valores ímpares são {valores_ímpares}')
