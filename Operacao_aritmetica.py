"""
Operações aritméticas

+ Adição
- Subtração
* Multiplicação
/ Divisão
% Módulo ou resto da divisão
** Potência
// Divisão inteira

print('Digite um número: ')
num1=int(input())

print('Digite outro número: ')
num2=int(input())
print('================')
print(num1+num2)
print('================')
print(num1-num2)
print('================')
print(num1*num2)
print('================')
print(num1/num2)
print('================')
print(num1**num2)
print('================')
print(num1//num2)
print('================')
print(num1%num2)

============================================
ORDEM DE PRECEDÊNCIA
1 - ()
2 - **
3 - *, /, //, % (resolver primeiro o que vier na frente)
4 - + e -
============================================
UMA FORMA DE CALCULAR RAIZ QUADRADA
81**(1/2)
25**(1/2)

Raíz Cúbica
90**(1/3)

Pela ordem de precedência, o calculo é realizado dentro dos parenteses primeiro.

==============================================
INFORMAÇÃO PERTINENTE
, END=' ' SERVE PARA JUNTAR DOIS PRINTS (EVITA A QUEBRA DE LINHA)
\n = quebra de linha

"""
n=int(input("Digite um valor: "))
n2=int(input('Digite outro valor: '))

s=n+n2
m=n*n2
d=n/n2
e=n**n2

print(f'A soma é {s},o produto é {m}, e a divisão é {d:.3f}, a potenciação é {e}.') # Nesse trecho do código: {d:.3f} estou dizendo para o programa, quantas casas decimais eu quero que ele print e o tipo de valor (real ou inteiro)