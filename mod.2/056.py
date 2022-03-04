"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

> A média de idade do grupo.
> Qual é o nome do homem mais velho
> Quantas mulheres tem menos de 20 anos.
"""
soma = 0
nomemv =''
maioridhomem = 0
totmulher = 0
for p in range(1, 5):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Informe seu sexo [M/F]: '))
    print('=-=-=' * 3)
    soma = soma + idade
    if p == 1 and sexo in 'Mm':
        maioridhomem = idade
        nomemv = nome
    if sexo in 'Mm' and idade > maioridhomem:
        maioridhomem = idade
        nomemv = nome
    if sexo in 'Ff' and idade < 20:
        totmulher = totmulher + 1
media = soma/4
print(f'A média de idade do grupo é de {media} anos.')
print('O homem mais velho tem {} e se chama {}'.format(maioridhomem, nomemv))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher))