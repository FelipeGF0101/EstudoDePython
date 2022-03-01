"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

Ex: Apos a sopa
Ex: A sacada da casa
Ex: A torre da derrota
Ex: O lobo ama o bolo
Ex: Anotaram a data da maratona

frase = "Apos a sopa"
print(frase[::-1])
"""
frase = input('Insira a frase: ').strip().upper() # Elimina os espaços nas laterais e coloca tudo em maiusculo
palavra = frase.split() # Separa todas as partes da string numa lista
junto = ''.join(palavra) # Junta tudo em uma só string
inverso = ''
for letra in range(len(junto)-1, -1, -1): # Inverte toda a string
    inverso += junto[letra]
if inverso == junto:
    print(f'{frase}, {inverso}')
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palídrneomo ')