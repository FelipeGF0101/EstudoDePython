"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual doi o número escolhido pelo computador.

> o programa deverá escrever na tela se o usuário venceu ou perdeu.

"""
import random
import emoji

nome = input('Digite seu nome: ')
print('-=-*-=-*-' * 10)
print(f'{nome}, agora nós vamos brincar de advinhação.')
print('-=-*-=-*-' * 10)
print('Estou pensando em um número aleatório entre 0 e 5. Quero que você advinhe que número  é esse!')
print('-=-*-=-*-' * 10)
num = random.randint(0, 5)

num1 = int(input('Escolha um número: '))

if num1 == num:
    print(emoji.emojize("Você acertou!!🥳"))
else:
    print("Não foi dessa vez!")

print('-=-*-=-*-' * 10)
