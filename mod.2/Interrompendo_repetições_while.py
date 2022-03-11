"""
Laços de repetição

Interrompendo repetições do while.

cont = 1
while True:
    print(cont, ' => ', end='')
    cont = cont + 1
print('ACABOU')

=======================================
n = 0
soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma = soma + n
print(f'A soma vale {n}')

"""
