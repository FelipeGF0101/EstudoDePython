'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados em ordem crescente.
'''
valores = []
resp = ''
while resp != 'N':
    num = int(input('Insira um valor: '))
    if num not in valores:
        valores.append(num)
    else:
        print('Valor existente. Adicione outro valor...')
    resp = input('Deseja continuar? [S/N]: ').upper()
    
valores.sort()
print(valores)
