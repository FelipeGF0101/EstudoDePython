# Condição simples

nome = input('Qual é o seu nome? ')
if nome.upper() == 'FELIPE':
    print('Que nome bonito!')
print(f'Tenha um bom dia, {nome}!')

# Condição composta

nome = input('Qual é o seu nome? ')
if nome == 'Felipe':
    print('Que nome bonito!')
else: 
    print('Seu nome é bem comum.')
print(f'Tenha um bom dia, {nome}!')

# Condição aninhada

nome = input('Qual é o seu nome? ')
if nome == 'Felipe':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
else: 
    print('Seu nome é bem comum.')
print(f'Tenha um bom dia, {nome}!')
