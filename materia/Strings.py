# Resumo dos conceitos de strings e métodos built-in em Python

# Conceito de String
# Uma string é uma cadeia de caracteres, isto é, consiste numa sequência de caracteres.
# O conteúdo de uma string está entre aspas duplas (" ") ou aspas simples (' ').
# Uma string sem quaisquer caracteres consiste numa string nula.

# Exemplo de criação de strings
string1 = "Olá, mundo!"
string2 = 'Python é incrível!'
string_vazia = ""

# Concatenação de strings
# Concatenação de strings é uma operação que pode ser vista como uma operação análoga à adição na matemática.
string_concatenada = string1 + " " + string2
print(string_concatenada)  # Saída: Olá, mundo! Python é incrível!

# Índice de uma string
# Uma string consiste num conjunto de caracteres, acessíveis individualmente através da especificação do seu índice (posição) na string.
# O primeiro caractere de uma string tem a posição 0.

primeiro_caractere = string1[0]
print(primeiro_caractere)  # Saída: O

# Substring: subconjunto de caracteres de uma string
# Podemos extrair substrings de uma string, explicitando o tamanho da substring através de [posição_inicial:posição_final]

substring = string1[0:5]
print(substring)  # Saída: Olá,

# Substring com índices negativos
substring_negativa = string1[-6:]
print(substring_negativa)  # Saída: mundo!

# Comprimento de uma string
# A função len() devolve o comprimento da string (número de caracteres).

comprimento = len(string1)
print(comprimento)  # Saída: 11

# Percorrer a sequência de caracteres de uma string
for caractere in string1:
    print(caractere, end=" ")  # Saída: O l á ,   m u n d o !

print()  # Nova linha

# Métodos built-in Python para manipulação de strings

# upper() - Devolve uma string com todos os caracteres em maiúsculas
maiuscula = string1.upper()
print(maiuscula)  # Saída: OLÁ, MUNDO!

# lower() - Devolve uma string com todos os caracteres em minúsculas
minuscula = string1.lower()
print(minuscula)  # Saída: olá, mundo!

# find(padrao) - Devolve a posição em que se encontra, na string, o padrão de procura (primeira ocorrência). Se não existir devolve -1.
posicao_find = string1.find("mundo")
print(posicao_find)  # Saída: 6

# index(padrao) - Devolve a posição em que se encontra, na string, o padrão de procura (primeira ocorrência). Se não existir dá erro!
posicao_index = string1.index("mundo")
print(posicao_index)  # Saída: 6

# rfind(padrao) - Devolve a posição em que se encontra, na string, o padrão de procura (última ocorrência)
posicao_rfind = string1.rfind("o")
print(posicao_rfind)  # Saída: 10

# rindex(padrao) - Devolve a posição em que se encontra, na string, o padrão de procura (última ocorrência)
posicao_rindex = string1.rindex("o")
print(posicao_rindex)  # Saída: 10

# split(caracter) - Divide uma string em substrings, em função do caracter especificado
substrings = string1.split(",")
print(substrings)  # Saída: ['Olá', ' mundo!']

# replace(s1, s2) - Devolve uma string em que todas as ocorrências de s1 são substituídas por s2
string_replace = string1.replace("mundo", "Python")
print(string_replace)  # Saída: Olá, Python!

# count(padrao) - Devolve o número de ocorrências de um padrão na string
contagem = string1.count("o")
print(contagem)  # Saída: 2

# strip() - Remove espaços em branco no início e fim da string
string_com_espacos = "   Olá, mundo!   "
string_sem_espacos = string_com_espacos.strip()
print(string_sem_espacos)  # Saída: Olá, mundo!

# startswith(padrao) - Devolve True se a string se inicia com o padrão de pesquisa. Caso contrário devolve False.
inicia_com_ola = string1.startswith("Olá")
print(inicia_com_ola)  # Saída: True

# Exercícios para avaliar o conhecimento sobre strings

def avaliar_conhecimento():
    nome = input("Digite um nome: ")
    print(f"Número de caracteres: {len(nome)}")
    print(f"Número de espaços: {nome.count(' ')}")

    nome_completo = input("Digite um nome completo: ")
    primeiro_nome = nome_completo.split()[0]
    ultimo_sobrenome = nome_completo.split()[-1]
    print(f"Primeiro nome próprio: {primeiro_nome}")
    print(f"Último sobrenome: {ultimo_sobrenome}")

avaliar_conhecimento()
