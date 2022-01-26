"""
Cores no terminal

ANSI
Escape sequence

# PESQUISAR MÓDULO COLORIZE

\033[código m

\033[style;text;backm

style:
> 0 (significa nada)
> 1 (texto em negrito)
> 4 (Underline)
> 7 (inverte tudo)

text: existem outras cores
> 30 (branco)
> 31 (vermelho)
> 32 (verde)
> 33 (amarelo)
> 34 (azul)
> 35 (roxo)
> 36 (ciano)
> 37 (cinza)

Back: segue o mesmo padrão de cores acima 
> 40 
...
> 47
"""
print('\033[1;34;41mFelipe Guedes\033[m')

print('\033[1;34;43mYuri Felipe Guedes Fernandes\033[m')

a = 'Felipe'
b = 'Guedes'

print(f'Seu primeiro nome é \033[1;33;45m{a}\033[m e o seu segundo nome é \033[1;31;45m{b}\033[m!')