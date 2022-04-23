'''
Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados.

B) A soma dos valores da terceira coluna.

C) O maior valor da seguda linha.

'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
somatcoluna = 0
segunda = 0


for l in range(0, 3): # linhas 
    for c in range(0, 3): # colunas
        matriz[l][c] = int(input(f'Insira um valor para {[l, c]}: ')) # preenchendo com valores
              
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c] % 2 == 0:
            soma = soma + matriz[l][c]  
    print()

print(soma)

for l in range(0, 3):
    somatcoluna += matriz[l][2]

print(somatcoluna)

for c in range(0, 3):
    if c == 0:
        segunda = matriz[1][c]
    elif matriz[1][c] > segunda:
        segunda = matriz[1][c]
    
print(segunda)

