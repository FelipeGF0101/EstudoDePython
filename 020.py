"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

"""
import random

alunoa = input("Digite seu nome: ")

alunob = input("Digite seu nome: ")

alunoc = input("Digite seu nome: ")

alunod = input("Digite seu nome: ")

lista = [alunoa, alunob, alunoc, alunod]

# O shuffle embaralha a lista
random.shuffle(lista)

print(f'A ordem de apresentação será essa: {lista}')


