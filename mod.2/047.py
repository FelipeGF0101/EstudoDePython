"""
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

"""
print('-=-=-=-=-=-=-= CONTANDO PARES -=-=-=-=-=-=-=-=')
for num in range(1, 51):
    if num % 2 == 0:
        print(f'\033[1;32m{num}\033[m', end=' ')

# Outra forma
#for cont in range(2, 52, 2):
#    print(cont, end=' ')