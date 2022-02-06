"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base conversão:

> 1 Para binário
> 2 Para octal
> 3 Para hexadecimal


"""
num = int(input('Insira um valor: '))
resp = str(input('Escolha para qual base numérica deseja converter [binário, octal ou hexadecimal]: ')).upper()
if resp == 'BINÁRIO':
    num = bin(num)
    print(num)
elif resp == 'OCTAL':
    num = oct(num)
    print(num)
elif resp == 'HEXADECIMAL':
    num = hex(num)
    print(num)

"""
Tipo de formatação	
=	Coloca o sinal na posição mais à esquerda
b	Converte o valor em binário equivalente
o	Converte o valor para o formato octal
x	Converte o valor para o formato Hex
d	Converte o valor dado em decimal
E	Formato científico, com um E em maiúsculas
X	Converte o valor para o formato Hex em maiúsculas

EXEMPLO:

temp = format(10, "b")

print(temp)

RESULTADO:

1010

Utilize o str.format() Método de conversão de int para binário em Python
O método str.format() é semelhante à função format() acima e partilham o mesmo format_spec.
O código de exemplo para converter int para binário utilizando o método str.format() está abaixo.

temp = "{0:b}".format(15)

print(temp)

RESULTADO
1111

"""