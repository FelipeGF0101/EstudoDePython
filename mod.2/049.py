"""
Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

"""
print('-=-=-=-=-=-=-=- TABUADA -=-=-=-=-=-=-=')
print('-=-=-=-=' * 5)
valor = int(input('Digite um valor: '))
for num in range(0, 11):
    result = valor * num
    print(f'{valor} X {num} = {result}')
