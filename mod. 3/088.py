'''
Faça um programa que ajude um jogador de MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

'''
import random
import time

print('GERADOR DE PALPITES DA MEGA SENA!')
print('=x=x'*10)

palpites = int(input('Quantos jogos gostaria de fazer? '))
for p in range(palpites):
    palp = random.sample(range(0, 61), 6)
    palp.sort()
    time.sleep(1)
    print(f'O {p + 1}º palpite é: {palp}')   
