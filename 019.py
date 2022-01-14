"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escolhendo o nome escolhido.

"""
import random
alunoA = input("Digite seu nome: ")
print("==============================")
alunoB = input("Digite seu nome: ")
print("==============================")
alunoC = input("Digite seu nome: ")
print("==============================")
alunoD = input("Digite seu nome: ")
print("==============================")

num = random.randrange(1,5)
print(f"O número sorteado foi: {num}")

print("==============================")

if num == 1:
    print(f"{alunoA}, o escolhido para apagar o quadro foi você.")
elif num == 2:
    print(f"{alunoB}, você foi o escolhido de hoje!")
elif num == 3:
    print(f"{alunoC}, hoje é a sua vez!")
elif num == 4:
    print(f"{alunoD}, você terá que apagar o quadro!")

"""
# Outra fomra

import random 

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: ))
n3 = str(input('Terceiro aluno: ))
n4 = str(input('Quarto aluno: ))

lista = [n1, n2, n3, n4]

escolhido = random.choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))

"""