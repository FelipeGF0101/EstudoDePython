"""
Condições simples e condições compostas

condicional if, else
"""
nome = (input('Qual o é o seu nome? ')).upper()
if nome == 'FELIPE':
    print('Que nome lindo você tem!')
else:
    print('Seu nome não é tão legal assim...')
print(f'Bom dia {nome.capitalize()}.')

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))

m = (n1 + n2)/2

print(f'Sua média foi {m:.1f}!')

if m >= 6: 
    print('Parabéns!')
else:
    print('Você se deu mal!')