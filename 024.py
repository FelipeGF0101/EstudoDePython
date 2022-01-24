"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'.

"""
cidade = input("Digite o nome da cidade: ")
# O split vai criar uma lista dividindo a string e vai verificar se na primeira posição existe a palavra 'santo'.
# O upper vai garantir que, não importa a forma como o usuário escreva, a palavra santo será reconhecida. Isso porque o upper vai deixar tudo em letras maiúsculas.
if cidade.split()[0].upper() == 'SANTO': 
    print('O nome da cidade começa com a palavra "Santo".')
else:
    print('O nome da cidade não tem "Santo".')

# Outra forma de fazer:

cid = input('Em que cidade você nasceu? ')
print(cid[:5].upper() == 'SANTO') # Aqui o programa apenas retornará False or True