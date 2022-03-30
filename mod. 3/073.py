'''
Crie um tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:

A) Apenas os 5 primeiros colocados. 
B) Os últimos 4 colocados da tabela
C) Uma lista com os times em ordem alfabética
D) Em que posição na tabela está o time da chapecoense.
'''
times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
 'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará SC', 
 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 
 'Bahia', 'Sport Recife', 'Chapecoense')

print(f'Os 5 primeiros colocados são {times[0:5]}')
print(f'Os 4 últimos colocados da tabela são {times[16:20]}') # Também poderia ser {times[-4]}
print('=============================================')
print(f'Organizando por ordem alfabética {(sorted(times))}.')
print(times.index('Chapecoense') + 1)