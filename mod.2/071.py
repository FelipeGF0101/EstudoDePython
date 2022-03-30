"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

-> OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.
"""
# SENHA 1234
import time
soma = saque = calc = 0
resposta = 'S'
conts = 1
cinquent = vint = dez = um = 0

print('\033[1;32m<==><==>\033[m' * 6)
print('\033[1;32m<==><==>\033[m' * 2,'-> BANCO DEV <-','\033[1;32m<==><==>\033[m' * 2,)
print('\033[1;32m<==><==>\033[m' * 6)
print('\033[1;32m<==><==>\033[m', 'BOM DIA! BEM VINDO AO BANCO DEV', '\033[1;32m<==><==>\033[m')
print('\033[1;32m<==><==>\033[m' * 6)
nome = input('INFORME SEU NOME: ').upper()
print(f'OLÁ, {nome}!')
print('\033[1;32m<==><==>\033[m' * 6)

senha = input('INFORME SUA SENHA NUMÉRICA DE 4 DÍGITOS: ')
print('\033[1;32m<==><==>\033[m' * 6)
print('VERIFICANDO...')
time.sleep(1)

while True:
    if senha == '1234':
        print('\033[1;32m<==><==>\033[m' * 6)
        opc = (input(""" 
        [ 1 ] => DEPÓSITO
        [ 2 ] => SALDO
        [ 3 ] => SAQUE
        [ 4 ] => FINALIZAR

        ESCOLHA UMA DAS OPÇÕES: """))
        print('\033[1;32m<==><==>\033[m' * 6)
        if opc == '1':
            print('VOCÊ ESCOLHEU A OPÇÃO DEPÓSITO... ')
            deposito = int(input('Informe o valor que deseja depositar R$ '))
            soma = soma + deposito
            time.sleep(1)
            print('CONFERINDO...')
            time.sleep(2)
            print('FINALIZADO!')
            print('\033[1;32m<==><==>\033[m' * 6)

        if opc == '2':
            print('VOCÊ ESCOLHEU A OPÇÃO SALDO... ')
            time.sleep(1)
            print('AGUARDE...')
            time.sleep(0.5)
            print(f'SEU SALDO ATUAL É DE R${soma} reais.')
            print('\033[1;32m<==><==>\033[m' * 6)
        
        if opc == '3':
            print('VOCÊ ESCOLHEU A OPÇÃO SAQUE...')
            saque = int(input('Qual valor deseja sacar? R$ '))

            while saque < 10 or saque > 700:
                print('SAQUE PERMITIDO PARA VALORES ACIMA DE R$ 10 E ABAIXO DE R$700!')
                saque = int(input('Qual valor deseja sacar? R$ '))
            
            if saque > soma:
                time.sleep(1)
                print('SEU SALDO É INSUFICIENTE!')
                print('\033[1;32m<==><==>\033[m' * 6)
            else:
                print('SAQUE LIBERADO!')
                print('\033[1;32m<==><==>\033[m' * 6)    
                calc = soma - saque
                soma = calc
                cinquent = int(saque/50)
                saque = saque % 50
                
                print(f'SAQUE EM {cinquent} NOTAS DE R$ 50')
                vint = int(saque/20)
                saque = saque % 20
                 
                print(f'SAQUE EM {vint} NOTAS DE R$ 20')
                dez = int(saque/10)
                saque = saque % 10
                
                print(f'SAQUE EM {dez} NOTAS DE R$ 10')
                um = saque
                
                print(f'SAQUE EM {um} NOTAS DE R$ 1')
                

        if opc == '4':
            print('ENCERRANDO ATENDIMENTO... TENHA UM BOM DIA!')
            break
    else:
        print('SENHA INCORRETA!')
        conts = conts + 1
        senha = input('INFORME SUA SENHA NUMÉRICA DE 4 DÍGITOS: ')
        if conts == 3:
            print('\033[1;31mCONTA BLOQUEADA! PARA DESBLOQUEAR, VÁ ATÉ UMA AGÊNCIA MAIS PRÓXIMA DE VOCÊ.\033[m')
            break
