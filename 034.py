"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

> para salários superiores a R$ 1.250,00, calcule um aumento de 10%.

> Para os inferiores ou iguais, o aumento é de 15%.
"""
sal = float(input('Digite o seu salário: '))
if sal > 1.250:
    sal = sal + (10/100*sal)
    print(f'O seu salário será de R$:{sal:.3f} reais.')
elif sal < 1.250:
    sal = sal + (15/100*sal)
    print(f'O seu salário será de R$: {sal:.3f} reais.')