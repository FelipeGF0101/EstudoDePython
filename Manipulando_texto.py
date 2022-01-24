"""
string indexada.
Cada caractere ou ou espaço recebe um índice:

python -> p y t h o n
          0 1 2 3 4 5

"""
#  FATIAMENTO DE STRING

frase = "Python"

print(frase[2]) # letra t

print(frase[0: 6]) # Usa-se dois pontos ':' para definir onde começar, onde parar e o passo (quantas casas saltar por exemplo)

frase1 = "Python é melhor linguagem"

print(len(frase1))

print(frase1[0:25]) # Sempre deve-se colocar um número a mais para conseguir imprimir toda a string

print(frase1[0:25:2]) # Inicio: final: pulo

print(frase1[:25]) # Nesse caso, quando não definimos um valor de incício, a contagem começa a partir do índice zero.

print(frase1[9:]) # Se eu der o valor de início, o valor de parada será o final.

print(frase1[9::2]) # Valor de incício (9), valor de final indefinido (ele vai até o final), pulo 2 (quantas casa pular)

# ANÁLISE

print(len(frase)) # conta quantas índices existem em determinada string

print(frase1.count('o')) # Vai contar quantas letras 'o' existem na string

print(frase1.count('o', 0, 13)) # Vai contar quantas letra 'o' existem dentro do limite estabelecido -> 0, 13 (início, parada)

print(frase1.find('lingua')) # Vai dizer onde começa e termina a sequência fornecida. 

print(frase.find('Java')) # Caso a string não exista o find retorna o valor -1

print('Python' in frase1) # O in vai dizer se tal sentença existe ou não dentro da string. Mas lembrando que a palavra ou caractere deve ser escrito exatamente igual ao que consta na variável, caso contrário a resposta pode vir errada. 

print('python' in frase1) # Aqui resulta false, pois a cadeia de caracteres 'Python' está escrito com letra maiúscula.

print(frase.replace("Python", "Android")) # O replace substitui um valor por outro

print(frase.upper()) # Muda todos os caracteres para maiúsculo.

print(frase.lower()) # Muda todos os caracteres para minúsculo.

print(frase1.lower().find('python')) # Posso utilizar duas funções ao mesmo tempo. 

print(frase.capitalize()) # Muda tudo para minúsculo e deixa apenas o primeiro caractere maiúsculo.

print(frase1.title()) # O title analisa quantas paravras existem na string e transforma o primeiro caractere de cada palavra em maiúsculo. 

print(frase1.strip()) # O strip analisa a string e exclui espaços excedentes ou desnecessários

print(frase1.rstrip()) # O rstrip funciona de forma semelhante ao strip, mas quando colocamos o r antes da função indica que deve começar pela direita, não alterando assim o início da string

print(frase1.lstrip()) # O lstrip funciona de forma semelhante ao strip, mas quando colocamos o l antes da função indica que deve começar pela esquerda, não alterando assim o final da string

# Algumas funções do python podem ser usadas colocando o r ou o l antes. Indicando se deve começar pela direita ou esquerda.

print(frase1.split()) # O split faz a divisão de strings de toda a cadeia de caractere. Ele cria uma lista com todas a novas strings.

print(''.join(frase1)) # O join faz a junção de strings. Entre as aspas eu poderia colocar como gostaria de juntar as strings. Poderia ser por espaços em brancos ou hífens...

