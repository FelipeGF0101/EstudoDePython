"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

> Se ele ainda vai se alistar aos serviço militar
> Se é a hora de se alistar.
> Se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

"""
import time
print('============ ALISTAMENTO OBRIGATÓRIO ============')
print('==========' * 5)
nome = input('Nome Completo: ')
print('==========' * 5)
idade = int(input('Ano de nascimento: '))
print('==========' * 5)
print(f'{nome}, todo brasileiro do sexo masculino, no ano em que completa 18 anos, deve se alistar, obrigatoriamente, no Serviço Militar. Esse alistamento é obrigatório inclusive aos portadores de deficiência física e mental.')
print('==========' * 5)
print('Analisando informações...')

# Poderia usar o 'from datetime import date' e 'atual = date.today().year'. O programa sempre iria o usar o ano atual.
calc = 2022 - idade
time.sleep(4)
print('==========' * 5)

if calc < 18:
    print(f'{nome}, você tem {calc} anos. A sua vez de se alistar ainda não chegou. Mas fique atento para não perder o prazo!')
elif calc >= 18 and  calc < 19:
    print(f'{nome}, a sua vez chegou! Apresente-se a Junta de Serviço Militar mais próxima a sua residência.')
elif calc > 19:
    print(f'{nome}, VOCÊ PERDEU O PRAZO PARA O ALISTAMENTO.\nQuem não se alista dentro do prazo tem que pagar uma multa de R$ 4,50 que é reajustada de três em três meses pelo IPCA-E (Índice Nacional de Preços ao Consumidor Amplo Especial). Além da multa, quem não se alista no prazo estará em débito com o Serviço Militar e não poderá:')
    print('==========' * 5)
    print('* Prestar exame ou matricular-se em qualquer estabelecimento de ensino;')
    print('* Fazer passaporte ou prorrogar sua validade;')
    print('* Ingressar como funcionário, empregado ou associado em  instituição, empresa ou associação oficial, oficializada ou subvencionada;')
    print('* Assinar contrato com o Governo Federal, Estadual, dos Territórios ou Municípios;')
    print('* Obter carteira profissional, registro de diploma de profissões liberais, matrícula ou inscrição para o exercício de qualquer função e licença de indústria e profissão;')
    print('Entre outros...')
