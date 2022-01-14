"""
Formas de utilização:
forma1 = import (nome da biblioteca)
por exemplo: import math ---> Neste caso, todas as funcionalidades embutidas nesta biblioteca serão importadas para o meu programa.

forma2 = from (nome da biblioteca) import (funcionalidade)
por exemplo: from math import sqrt ---> Neste caso, importa-se somente a função escolhida pelo desenvolvedor dentro da biblioteca. 

FORMA 1
# Exemplo1

import math 

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {raiz}.')

# Resultado: 
# Digite um número: 81
# A raiz de 81 é igual a 9.0.

# Exemplo2

import math 

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {math.ceil(raiz)}.') # Usando uma formatação diferente. Utilizando nome da biblioteca + função 'ceil'(arredonda para cima) + variável entre parênteses. Aplicação interessante em casos de resultado com muitas casas decimais.

# Resultado:
# Digite um número: 29
# A raiz de 29 é igual a 6.

# A raiz quadrada de 29 resulta em: 5.385164807134504, porém, utilizando a função ceil, o resultado vai para 6.

# Uma outra forma de fazer: 
# print(f'A raiz de {num} é igual a {raiz:.2f} Neste caso o resultado seria: 5.39

========================================================================================

# FORMA 2

# Exemplo1

from math import sqrt # Importação da biblioteca junto com apenas uma funcionalidade

num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz de {num} é igual a {raiz}.')

# Exemplo2

from math import sqrt, floor #(Arredonda para baixo)
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz de {num} é igual a {floor(raiz):.2f}.') # Quando fazemos a importação de uma única funcionalidade da biblioteca, não há mais necessidade de escrever o nome da biblioteca. + funcionalida.

==========================================================

import random 

num = random.random() # Gera um número aleatório. Como não estabalecemos um início nem um valor final, ele vai gerar um valor entre 0 e 1.

print(num)

num2 = random.randint(1, 10) # Gera um número entre 1 e 10.
print(num2)
"""
import emoji

print(emoji.emojize("Olá Mundo :smiling_imp:", use_aliases=True))

