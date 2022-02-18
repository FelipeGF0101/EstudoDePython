"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: 

> À vista dinheiro/cheque: 10% de desconto
> À vista no cartão: 5% de desconto
> Em até 2x no cartão: preço normal
> Em 3x ou mais no cartão: 20% de juros

"""
nome = str(input('Digite seu nome: '))
nome = nome.capitalize()
print('======' * 5)
valor = float(input('Informe o valor do produto R$ '))
print('======' * 5)
pag = str(input('Escolha a forma de pagamento. Dinheiro/Cheque(1), Cartão à vista(2), Até duas X no cartão(3), Três X ou mais no cartão(4): '))
print('======' * 5)
if pag == '1':
    valor = valor - (10/100) * valor
    print(f'{nome}, a forma de pagamento escolhida gera um desconto de 10% no valor do produto. O valor a ser pago será de R${valor:.2f}.')
elif pag == '2':
    valor = valor - (5/100) * valor
    print(f'{nome}, a forma de pagamento escolhida gera um desconto de 5% no valor do produto. O valor a ser pago será de R${valor:.2f}.')
elif pag == '3':
    print(f'{nome}, a forma de pagamento escolhida não gera nenhum desconto ou acréscimo no valor do produto. O valor a ser pago será de R${valor:.2f}.')
    valparc1 = valor/2
    print(f'Cada parcela terá o valor de R$ {valparc1:.2f} ')
elif pag == '4':
    valor = valor + (20/100) * valor
    print(f'{nome}, a forma de pagamento escolhida gera um acréscimo de 20% no valor do produto. O valor a ser pago será de R${valor:.2f}.')
    totparc = int(input('Informe a quantidade de parcelas: '))
    valparc = valor/totparc
    print(f'O valor de cada parcela será de R$ {valparc:.2f}')
print('======' * 5)
print('Agradecemos pela preferência!')
