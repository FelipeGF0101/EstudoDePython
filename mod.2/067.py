"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

"""
print('=-=' * 6, 'TABUADA' , '=-=' * 6,)
print('=-=' * 15)
cont = 0
while True:
    n = int(input('Deseja ver a tabuada de qual valor? '))
    print('=-=' * 15)
    if n < 0:
        print('FIM')
        break
    cont = 0

    while cont < 10:
        cont = cont + 1
        result = n * cont
        print(f'{n} X {cont} = {result}')

print('=-=' * 15)

"""
OUTRA POSSIBILIDADE

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}')
    print('-' * 30)
print('Programa tabuada encerrado. Volte sempre!')
"""