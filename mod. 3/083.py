'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

'''
valores = []
resp = ''
cont = 0
while resp != 'N':
    valores = input('Digite uma expressão numérica: ')
    cont1 = valores.count('(')
    cont2 = valores.count(')')
    cont = cont1 + cont2
    
    if cont % 2 == 0:
        print(f'A expressão {valores} está com os parênteses em ordem!')
    else:
        print(f'A expressão {valores} não está em ordem!')
    resp = input('Deseja continuar? [S/N]: ').upper()

print('FIM!')
# Minha resolução está errada porque ela só verifica a quantidade correspondente de parênteses na expressão, não levando em conta a ordem de ocorrência.

# RESOLUÇÃO DO GUANABARA

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão não é válida!')