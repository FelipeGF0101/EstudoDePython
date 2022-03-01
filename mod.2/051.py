"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA (progressão aritmética.). No final, mostre os 10 primeiros termos dessa progressão.

"""
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da pa: '))
decimo = a1 + (11 - 1) * r # fórmula para calcular um pa
for c in range(a1, decimo, r):
    print(f'{c}', end= '-> ')
print('ACABOU!')