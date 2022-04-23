'''
Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

'''
lista = list()

while True:
    qtde = int(input('Quantos alunos gostaria de adicionar? '))
    for i in range(qtde):
        print('=x=x' * 10)
        nome = str(input(f'Informe o nome do {i+1}º aluno: ')).capitalize()
        nota1 = float(input('Informe a primeira nota: '))
        nota2 = float(input('Informe a segunda nota: '))
        media = (nota1 + nota2) / 2
        lista.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja adicionar mais alunos [S/N]? ')).upper().strip().capitalize()
    if resp != 'S':
        break
        
print('=x=x' * 10)
print('=x=x' * 3, ' BOLETIN ', '=x=x' * 4 )    
print(f'{"Nº":<4}{"NOME":>6}{"MÉDIA":>15}')
print('=x=x' * 10)
for i, nome in enumerate(lista):
    print(f'{i:<4} {nome[0]:<10} {nome[2]:>8.1f}')
print('=x=x' * 10)

while True:
    ver_notas = str(input('Gostaria de ver as notas de algum aluno [S/N]? ')).upper().strip().capitalize()
    if ver_notas != 'S':
        break
    else:
        op = int(input('Informe o número correspondente do aluno (para emcerrar digite 999): '))
        if op == 999:
            break
        if op <= len(lista) -1:
            print(f'As notas de {lista[op][0]} são {lista[op][1]}')
print('=x=x' * 10)
print('FINALIZANDO SISTEMA!')
