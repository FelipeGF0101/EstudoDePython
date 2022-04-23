'''
Listas = São mutáveis! Diferentemente das tuplas

métodos:
append() -> Adiciona valor ao final da lista
insert() -> Insere um valor na lista informando o indice e o que entrará na lista no espaço escolhido. 
Exemplo: insert(0,'burrito') 


lista = ['hamburguer', 'suco', 'pizza']
lista.insert(0, 'cookie')
print(lista)


# APAGANDO VALORES DE UMA LISTA
# del lanche[3]
del lista[0]
print(lista)

#lanche.pop(3)
lista.pop(1)
print(lista)

#lanche.remove('pizza')
# Com o remove(), não utilizamos o indice, mas sim o próprio valor que desejamos apagar.
lista.remove('pizza')
print(lista)

# Utilizando o pop() sem passar nenhum parametro(indice), ele irá apagar o último valor da lista.
lista.pop()
print(lista)

# Caso um valor que foi passado não exista na lista, a linguagem retornará um erro. Para evitar esse tipo de coisa, podemos utilizar o if e o in. 
# Exemplo:
if 'pizza' in lista:
    lista.remove('pizza')

# CRIANDO LISTA COM RANGE

valores = list(range(1, 11))
print(valores)

# ORGANIZANDO UMA LISTA
# Usando o sort()

valores1 = [8, 2, 5, 4, 9, 3, 0]
valores1.sort()
print(valores1)

# Organizando de forma inversa com o método sort()
valores1.sort(reverse=True)
print(valores1)

# CONTANDO VALORES EM UMA LISTA
# len()

print(len(valores1))

ALGUNS TESTES:

num = [2, 5, 9, 1]
print(num)

num[2] = 3
num.append(7)
print(num)

num.sort(reverse=True)
print(num)

num.insert(2, 0)
print(num)

print(f'Essa lista tem {len(num)} elementos.')

# Removendo elementos
#num.pop()
print(num)

num.pop(2) # Usando o indice '2' ele irá remover o valor na posição 2.
print(num)

'''
valores = []
for num in range(0, 4):
    valores.append(int(input('Digite um valor: ')))
print(valores)
