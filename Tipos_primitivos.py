"""Tipos primitivos"""

# n1=input('Digite um número: ') -> n1=input('Digite um número: ') Neste formato, o valor digitado será interpretado como uma string e desta forma a soma entre dois números como 2 e 2 por exemplo, teria como resultado o número 22 e não 4. Por isso é necessário o uso do tipo primitivo 'int'.

n1=int(input('Digite um número: '))
n2=int(input('Digite mais um número: '))
s=n1+n2

print(f'O resultado da soma de {n1} e {n2} é: {s}')

# Existem 4 tipos primitivos básicos em python.
# São eles:
#int: números inteiros tipo: 7, -4, 0, 9875
#float: números reais tipo: 4.5, 0.076, 7.0
#bool: valores boleanos tipo: True(verdadeiro), False(falso)
#str: string tipo:'Olá', 'Bom dia', '7.5', '', '900'.

n3 = int(input('Digite um valor: '))
print(type(n3)) # Para saber o tipo primitivo do valor.
