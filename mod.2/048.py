"""
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

"""
print('-=-=-=-=-= MÚLTIPLOS DE TRÊS -=-=-=-=-=-')
for num in range(1, 500):
    if num % 3 == 0:
        print(num)