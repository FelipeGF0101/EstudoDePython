"""
Faça um programa que leia uma frase pelo teclado e mostre:

> Quantas vezes aparece a letra 'A'

> Em que posição ela aparece a primeira vez

> Em que posição ela aparece a ultima vez

"""
frase = input("Digite a uma frase: \n").strip().upper()

print('A letra "A" aparece {} vezes.'.format(frase.count('A')))
print('A primeira letra "A" apareceu na posição {}'.format(frase.find('A'))) 
print('A última letra "A" apareceu na posição {}'.format(frase.rfind('A'))) # O rfind vai começar a procurar pela direita.

# Poderia ser assim:
# Acrescentando o mais +1 o programa vai começar a contagem a partir do 1 e não do 0
#print('A primeira letra "A" apareceu na posição {}'.format(frase.find('A')+1)) 
#print('A última letra "A" apareceu na posição {}'.format(frase.rfind('A')+1))