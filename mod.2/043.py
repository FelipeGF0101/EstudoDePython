"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

> Abaixo de 18.5: Abaixo do peso
> Entre 18.5 e 25: Peso ideal
> De 25 até 30: Sobrepeso
> De 30 até 40: Obesidade
> Acima de 40: Obesidade mórbida

"""
print('\033[1;36;45m========== IMC ==========\033[m')
nome = input('Digite seu nome: ')
print('======' * 5)
peso = float(input('Informe seu PESO: '))
print('======' * 5)
altura = float(input('Informe sua ALTURA: '))
print('======' * 5)
calc = peso/(altura * altura)

if calc < 18.5:
    print(f'{nome}, o seu IMC corresponte a {calc:.1f}. Você está ABAIXO DO PESO!')
elif calc >= 18.5 and calc <= 25:
    print(f'{nome}, o seu IMC corresponte a {calc:.1f}. Você está com PESO IDEAL!')
elif calc >= 25 and calc <= 30:
    print(f'{nome}, o seu IMC corresponte a {calc:.1f}. Você está com SOBREPESO!')
elif calc >= 30 and calc <= 40:
    print(f'{nome}, o seu IMC corresponte a {calc:.1f}. Você está com OBESIDADE!')
elif calc > 40:
    print(f'{nome}, o seu IMC corresponte a {calc:.1f}. Você está com OBESIDADE MÓRBIDA!')
