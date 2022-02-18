"""
Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

> Equilátero: Todos os lados iguais
> Isósceles: Dois lados iguais
> Escaleno: todos os lados diferentes

"""
a = float(input('Digite o valor do lado A: '))
b = float(input('Digite o valor do lado B: '))
c = float(input('Digite o valor do lado C: '))

# Condição de existência de um triângulo: é preciso que quaisquer dois lados do triângulo sejam maiores que um terceiro lado.
if a + b > c and b + c > a and a + c > b:
    print('As medidas fornecidas PODEM FORMAR um triângulo!')
else:
    print('As medidas fornecidas NÃO PODEM FORMAR um triângulo!')
print('=====' * 5)
if a == b and b == c:
    print('Com as medidas fornecidas por você, podemos concluir que se trata de um TRIÂNGULO EQUILÁTERO!')
elif a == b or b == c or a == c:
    print('Com as medidas fornecidas por você, podemos concluir que se trata de um TRIÂNGULO ISÓSCELES!')
else:
    print('Com as medidas fornecidas por você, podemos concluir que se trata de um TRIÂNGULO ESCALENO!')
print('=====' * 5)
