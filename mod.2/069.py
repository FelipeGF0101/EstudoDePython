"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
(Cadastre a idade e o sexo apenas)

A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.

"""
contidade = contsexo = contmulher = 0

while True:
    idade = int(input('\033[1;32mInforme a idade:\033[m '))
    print('<=>=<=>' * 5)
    sexo = str(input('\033[1;32mInforme o sexo [M/F]: \033[m')).upper().strip()[0]
    print('<=>=<=>' * 5)

    if idade > 18:
        contidade = contidade + 1
    if sexo == 'M':
        contsexo = contsexo + 1
    if idade < 20 and sexo == 'F':
        contmulher = contmulher + 1
    resposta = str(input('\033[1;32mDeseja continuar? [S/N] \033[m')).upper().strip()[0]

    while resposta != 'S' and resposta != 'N':
        print('RESPONDA APENAS COM "S" OU "N"!')
        resposta = str(input('\033[1;32mDeseja continuar? [S/N] \033[m')).upper().strip()[0]
    print('<=>=<=>' * 5)
    
    if resposta == 'N':
        break
# Daqui pra baixo, cuida da parte da concordância.
if contidade == 1:
    pessoa = 'pessoa tem'
else:
    pessoa = 'pessoas têm'
if contsexo == 1:
    homem = 'homem foi'
else:
    homem = 'homens foram'
if contmulher == 1:
    mulher = 'mulher tem'
else:
    mulher = 'mulheres têm'
print(f'\033[1;32m{contidade} {pessoa} mais de 18 anos. {contsexo} {homem} cadastrados. {contmulher} {mulher} menos de 20 anos.\033[m')
  