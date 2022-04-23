'''
LISTAS DENTRO DE LISTAS

pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]

pessoa = []
for i in range(0, 3):
    nome = input('Insira seu nome: ')
    idade = int(input('Insira sua idade: '))
    cpf = int(input('Insira seu cpf: '))
    pes = [nome,idade, cpf]
    pessoa.append(pes)

print(pessoa)
=================================================

teste = list()
teste.append('Felipe')
teste.append(31)

galera = []
galera.append(teste[:]) # Cria um cópia da lista teste
teste[0] = 'Maria'
teste[1] = 22

galera.append(teste)
print(galera)

=============================================
lista = [['Yuri', 31], ['Felipe', 30], 
['Guedes', 29], ['Fernandes', 28]]

for p in lista:
    print(f'{p[0]} tem {p[1]} anos de idade.')

'''
galera = []
dados = []
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Informe sua idade: ')))
    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
    else:
        print(f'{p[0]} é menor de idade.')
