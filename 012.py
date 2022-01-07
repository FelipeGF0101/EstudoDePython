"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

"""

print('Informe o valor do produto: ')
valor=float(input())

print(f'R$: {valor}')

valf=valor-(5/100*valor)

print(f'O valor do produto é R$ {valor}. Aplicando-se o desconto de 5%, o valor final será de R$ {valf}')

# Invertendo o processo:

print('Informe o preço do produto: ')
prec=float(input())

print(f'R$ {prec}')
valf2=prec+(5/100*prec)

print(f'O valor do produto é de R$ {prec}. O valor final com acréscimo será de R$ {valf2}')

# Para saber o valor do acréscimo separadamente

valor1 = float(input("Informe o valor R$ "))

porc = float(input("Informe a porcentagem que deseja acrescentar: "))

result = valor1*porc/100

print(f"O valor do acréscimo será de:R$ {result}.")

resulto = valor1 + result

print(f"O valor total será de R$ {resulto}")