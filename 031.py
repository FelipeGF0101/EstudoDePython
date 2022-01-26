"""
Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas.

"""
import time
viagem = float(input('Quantos quilômetros até o destino final? '))
print("CALCULANDO...")
time.sleep(2)
if viagem <= 200:
    val1 = viagem * 0.50
    print(f'O valor total da sua viagem será de R$ {val1:.2f} reais.')
elif viagem > 200:
    val1 = viagem * 0.45
    print(f'A viagem te custará o valor de R$ {val1:.2f} reais.')


