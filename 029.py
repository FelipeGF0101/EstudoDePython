"""
Escreva um programa que leia a velocidade de um carro.

> Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

> A multa vai curstar R$ 7,00 por cada km acima do limite.

"""
velo = int(input("Informe a velocidade do carro: "))

if velo > 80:
    mult = (velo - 80) * 7
    print(f'Como o veículo excedeu o limite de velocidade, você será multado em R$ {mult:.2f} reais.')
else: # Aqui não é necessário o uso do else:. Poderia ser feito como uma condicional simples, usando apenas o if.
    print("Dirija com segurança!")