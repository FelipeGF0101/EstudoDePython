'''
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1])

print(lanche[1:3])

print(lanche[:2])

# lanche[1] = 'Refrigerante' -> Gera TypeError. As tuplas não aceitam atribuição de valor posteiror à declaração da variável.

for comida in lanche:
    if comida == 'Suco':
        print(f'Eu vou beber {comida}')
    else:
        print(f'Eu vou comer {comida}')
print('Comi pra caramba')

print('==============================')
for cont in range(0, len(lanche)):
    print(lanche[cont])

print('==============================')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

==================================================

# Organizando uma tupla
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

print(sorted(lanche)) # Lembrando que a tupla continua imutável, porém esse comando mostra a tupla organizada.
print(lanche)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b

print(c)
print(sorted(c))
print(len(c))
print(c.count(5))
print(c.index(8))
print(c.index(5, 1)) # Procura pelo indice do valor 5 a partir da posição 1

'''
# Tuplas aceitam vários tipos de dados

pessoa = ('Felipe', 31, 'M', 113)
# del(pessoa) # É possível deletar toda a tupla
print(pessoa)

# Não é possível excluir um único item de uma tupla
