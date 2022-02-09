"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário, se exceder, o empréstimo será negado.

"""
from time import sleep
print('======' * 10)
print('\033[1;33;46m========== BEM VINDO AO BANCO DEV ==========\033[m')
nome = input('==> Informe seu nome: ')
print(f'Seja bem vindo, {nome}!')
print('======' * 10)

valor = float(input('Por favor, informe o valor do imóvel R$ '))
print('======' * 10)

salar = float(input('Informe a sua renda mensal R$ '))

print('======' * 10)
print('ANALISANDO INFORMAÇÕES...')
sleep(2)

porcent = (30/100*salar)
print('======' * 10)
print(f'{nome}, o valor da parcela não pode exceder 30% do seu salário atual.')
print('======' * 10)

temp = int(input('Em quantos anos você gostaria de parcelar? '))
print('======' * 10)
if temp >= 10:
    novovalor = valor + (20/100*valor)
    print(f'\033[1;31;43mNo financiamento com prazo igual ou superior a 10 anos, incidirá sobre o valor do imóvel um acréscimo de 20%. O valor atualizado é de R$ {novovalor:.2f}\033[m')

    print('EM ANÁLISE...')
    sleep(5)
    
    qm = (temp*12)
    result = novovalor/qm

    if result > porcent:
        print(f'{nome}, infelizmente o valor da parcela foi de {result:.2f}. Este valor ultrapassa o percentual permitido para o financiamento.')
    else:
        print(f'{nome}, o financiamento foi aprovado! Parabéns por sua nova aquisição!!! Este é o valor atualizado da sua parcela R$ {result:.3f} ')
else:
    print('======' * 10)
    qm = (temp*12)
    result = valor/qm
    if result > porcent:
        print(f'{nome}, infelizmente o valor da parcela foi de {result:.2f}. Este valor ultrapassa o percentual permitido para o financiamento.')
    else:
        print(f'{nome}, o financiamento foi aprovado! Parabéns por sua nova aquisição!!!')
