"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

"""
nome = input('Digite seu nome: ').strip()

if 'Silva' in nome:
    print(f'{nome}, seu nome tem Silva.')
else:
    print(f'{nome}, seu nome não tem Silva.')

# A resolução acimna apresenta uma falha. Caso o usuário escreva diferente do 'Silva', o programa não reconhecerá a palavra.

# Forma sem erros:
nome = input('Digite seu nome: ').strip()

if 'SILVA' in nome.upper():# Muda todos os caracteres para maiúsculo. Dessa forma, independente do que o usuário escreva a verificação será correta
    print(f'{nome}, seu nome tem Silva.')
else:
    print(f'{nome}, seu nome não tem Silva.')


# Forma simplificada
nom = input('Informe seu nome: ').strip() # Para eliminar espaços desnecessários 
print('Seu nome tem Silva? {}'.format('SILVA' in nom.upper()))