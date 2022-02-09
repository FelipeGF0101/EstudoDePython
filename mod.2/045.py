"""
Crie um programa que faça o computador jogar Jokenpô (pedra, papel, tesoura) com você.

"""
import random

print('\033[1;36;41m========== JOKENPÔ ==========\033[m')
print('======' * 5)
print('VAMOS JOGAR!')
print('======' * 5)
num = int(input('Escolha PEDRA(1), PAPEL(2) OU TESOURA(3): '))

item1 = ' '

if num == 1:
    item1 = 'PEDRA'
elif num == 2:
    item1 = 'PAPEL'
elif num == 3:
    item1 = 'TESOURA'
print(f'\033[1;30;45mUSUÁRIO: {item1} \033[m')
print('======' * 5)

ppt = random.sample(range(1, 4), 1)

item = ''

if ppt == [1]:
    item = 'PEDRA'
elif ppt == [2]:
    item = 'PAPEL'
elif ppt == [3]:
    item = 'TESOURA'
print(f'\033[1;33;41mCOMPUTADOR: {item} \033[m')
print('======' * 5)

if ppt == [1] and num == 1 or ppt == [2] and num == 2 or ppt == [3] and num == 3:
    print(f'{item} X {item1} = EMPATE')
elif ppt == [1] and num == 2:
    print(f'{item} X {item1} = USUÁRIO VENCEU')
elif ppt == [1] and num == 3:
    print(f'{item} X {item1} = COMPUTADOR VENCEU')
elif ppt == [2] and num == 1:
    print(f'{item} X {item1} = COMPUTADOR VENCEU')
elif ppt == [2] and num == 3:
    print(f'{item} X {item1} = USUÁRIO VENCEU')
elif ppt == [3] and num == 1:
    print(f'{item} X {item1} = USUÁRIO VENCEU')
elif ppt == [3] and num == 2:
    print(f'{item} X {item1} = COMPUTADOR VENCEU')
print('======' * 5)


