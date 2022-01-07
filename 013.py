"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

"""
print('Funcionário, informe seu nome: ')
nome=str(input())

print(f'{nome}, informe seu salário para que eu possa calcular o valor com acréscimo.')
sal=float(input())

nsal=sal+(15/100*sal)

print(f'{nome} o valor do seu salário somado com o acréscimo será de R$ {nsal:.3f}.')