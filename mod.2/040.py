"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

> Média abaixo de 5.0: Reprovado
> Média entre 5.0 e 6.9: Recuperação
> Média 7.0 ou superior: Aprovado


"""
import time
nome = input('Digite seu nome: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
print('==========' * 5)
print(f'{nome}, agora vou calcular a sua média. Aguarde alguns instantes!')
time.sleep(4)
media = (nota1 + nota2)/2
print(f'A sua média é {media}.')
print('==========' * 5)
if media < 5: 
    print('REPROVADO!')
elif media > 5 and media <6.9:
    print('RECUPERAÇÃO!')
elif media >= 7:
    print('APROVADO!')