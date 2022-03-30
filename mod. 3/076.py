'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 

No final, mostre uma listagem de preços, organizando os dados em forma tabular.

'''
produtos = ('Iphone', 6000, 'TV', 2500, 'Geladeira', 4000, 'Microondas', 600, 'Bicicleta', 1500, 'Fogão', 1000)

print('=+=' * 3, 'TABELA DE PREÇOS', '=+=' * 3) # PODERIA SER PRINT(F'{TABELA DE PREÇOS:^40}')

for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<30}', end='')
    else:
        print(f'R$ {produtos[item]:>5.2f}')
    
