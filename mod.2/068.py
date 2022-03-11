"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jojogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

"""
import random
print('\033[1;31m=^=^=^\033[m'*10)
print('\033[1;31m=^=^=^\033[m'*3, ' JOGO DO PAR OU ÍMPAR ', '\033[1;31m=^=^=^\033[m'*3)
print('\033[1;31m=^=^=^\033[m'*10)

cont = 0
while True:
    pc = random.randint(0, 10)
    escolha = str(input('Escolha PAR ou ÍMPAR [P/I]: ')).upper().strip()[0]
    while escolha != 'P' and escolha != 'I':
        print('\033[1;31mUSE APENAS A LETRA "P" OU "I(SEM ACENTO)!"\033[m')
        escolha = str(input('Escolha PAR ou ÍMPAR [P/I]: ')).upper().strip()[0]
    print('\033[1;31m=^=^=^\033[m'*10)

    n = int(input('Digite um valor: '))
    while n > 10 or n < 0:
        print('\033[1;31mESCOLHA UM VALOR ENTRE 0 E 10\033[m')
        n = int(input('Digite um valor: '))   
    print('\033[1;31m=^=^=^\033[m'*10)
    calc = pc + n

    if escolha == 'P' and calc % 2 == 0:
        cont = cont + 1
        print(f'\033[1;33;41mPARABÉNS! VOCÊ GANHOU UM PONTO! VOCÊ TEM {cont} PONTOS ACUMULADOS\033[m')
        print(f'\033[1;33mO COMPUTADOR ESCOLHEU {pc}\033[m')
    if escolha == 'P' and calc % 2 != 0:
        print('\033[1;30;42mCOMPUTADOR VENCEU!\033[m')
        break
    if escolha == 'I' and calc % 2 != 0:
        cont = cont + 1
        print(f'\033[1;33;41mPARABÉNS! VOCÊ GANHOU UM PONTO! VOCÊ TEM {cont} PONTOS ACUMULADOS\033[m')
        print(f'\033[1;33mO COMPUTADOR ESCOLHEU {pc}\033[m')
    if escolha == 'I' and calc % 2 == 0:
        print('\033[1;30;42mCOMPUTADOR VENCEU!\033[m')
        break
       