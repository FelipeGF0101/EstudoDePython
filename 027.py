"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

Ex: Ana Maria de Souza
Primeiro: Ana
Último: Souza

"""
nome = str(input('Digite seu nome completo: ')).strip().split() # O strip vai retirar espaços desnecessários da string. O split vai dividir a string em uma lista.

print('Seu primeiro nome é: {}'.format(nome[0])) # Nome na posição zero (que será o primeiro nome)
print('Seu último nome é: {}'.format(nome[len(nome)-1])) 

