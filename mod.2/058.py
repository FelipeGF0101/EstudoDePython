"""
Melhore o jogo do DESAFIO 028 onde o computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai tentar advinhar até acertar mostrando no final quantos palpites foram necessários para vencer.

"""
cont = 1
import random
usu = input('\033[1;32;41mDigite seu nome:\033[m ').capitalize()

print('=-=-=-=-=' * 4)

escnum = int(input(f'\033[1;32;41m{usu}, escolha um número de 0 a 10:\033[m '))
print('=-=-=-=-=' * 4)

num = random.randint(0, 10)
print(f'\033[1;31;43mO número escolhido pelo computador foi {num}\033[m')
print('=-=-=-=-=' * 4)

while escnum != num: 
    num = random.randint(0, 10) # O programa vai sortear um valor diferente pra cada vez que o usuário errar o palpite!
    escnum = int(input('\033[1;32;41mNÚMERO ERRADO! Escolha outro número de 0 a 10:\033[m '))
    print('=-=-=-=-=' * 4)
    print(f'\033[1;31;43mO número escolhido pelo computador foi {num}\033[m')
    print('=-=-=-=-=' * 4)
    if escnum != num or escnum == num:
        cont = cont + 1


print(f'\033[1;32;41m{usu}, você precisou de {cont} palpites para conseguir acertar!\033[m')

"""
CÓDIGO DO GUANABARA

from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi? ')
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais um vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')
"""
