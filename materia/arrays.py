# ALGORITMIA E ESTRUTURAS DE DADOS
# ESTRUTURAS DE DADOS NÃO PRIMITIVAS | LISTAS MULTIDIMENSIONAIS
# LICENCIATURA EM TECNOLOGIAS E SISTEMAS DE INFORMAÇÃO PARA A WEB
# #ESMAD #P.PORTO
# POLITÉCNICO DO PORTO
# ESCOLA SUPERIOR DE MEDIA ARTES E DESIGN

# 1. Arrays | Listas Bidimensionais

# Conceito:
# Uma lista bidimensional é uma lista de listas, similar a uma tabela com linhas e colunas.

# Índices:
# Cada elemento é acessado usando dois índices: um para a linha e outro para a coluna.

# Percorrer uma lista:
# Pode-se iterar sobre uma lista bidimensional como um objeto único, linha a linha, ou através dos índices.

# Criando uma lista bidimensional
lista_bidimensional = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Iterando sobre a lista bidimensional como um objeto único
print("Iterando sobre a lista bidimensional como um objeto único:")
for linha in lista_bidimensional:
    print(linha)

# Iterando sobre a lista bidimensional linha a linha
print("\nIterando sobre a lista bidimensional linha a linha:")
for linha in lista_bidimensional:
    for elemento in linha:
        print(elemento, end=' ')
    print()

# Iterando sobre a lista bidimensional através dos índices
print("\nIterando sobre a lista bidimensional através dos índices:")
for i in range(len(lista_bidimensional)):
    for j in range(len(lista_bidimensional[i])):
        print(lista_bidimensional[i][j], end=' ')
    print()

# Input de uma lista bidimensional
print("\nInput de uma lista bidimensional:")
linhas = 3
colunas = 3
lista_input = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        elemento = int(input(f"Digite o elemento para a posição [{i}][{j}]: "))
        linha.append(elemento)
    lista_input.append(linha)
print("Lista bidimensional criada pelo usuário:")
print(lista_input)

# Função que cria uma lista com determinada dimensão
def criar_lista_bidimensional(linhas, colunas):
    return [[0 for _ in range(colunas)] for _ in range(linhas)]

lista_criada = criar_lista_bidimensional(4, 5)
print("\nLista bidimensional criada com função:")
print(lista_criada)

# Funções built-in Python funcionam em listas de uma dimensão
lista_unidimensional = [1, 2, 3, 4, 5]
print("\nFunções built-in Python em listas de uma dimensão:")
print("Soma:", sum(lista_unidimensional))
print("Máximo:", max(lista_unidimensional))
print("Mínimo:", min(lista_unidimensional))

# 2. Arrays | Listas Tridimensionais

# Conceito:
# Uma lista tridimensional é uma lista que contém linhas, colunas e profundidade, como um cubo.

# Índices:
# Cada elemento é acessado usando três índices.

# Criando uma lista tridimensional
lista_tridimensional = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

# Iterando sobre a lista tridimensional
print("\nIterando sobre a lista tridimensional:")
for plano in lista_tridimensional:
    for linha in plano:
        for elemento in linha:
            print(elemento, end=' ')
        print()
    print()

# Exemplos de aplicabilidade:
# Parque de estacionamento com vários pisos, filas e lugares
parque_estacionamento = [
    [["Vazio", "Carro"], ["Moto", "Vazio"]],
    [["Carro", "Vazio"], ["Vazio", "Carro"]]
]
print("\nParque de estacionamento:")
for piso in parque_estacionamento:
    for fila in piso:
        for lugar in fila:
            print(lugar, end=' ')
        print()
    print()

# Representação de produtos numa máquina de vending
maquina_vending = [
    [["Água", "Refrigerante"], ["Suco", "Chá"]],
    [["Chocolate", "Biscoito"], ["Batata", "Amendoim"]]
]
print("\nMáquina de vending:")
for prateleira in maquina_vending:
    for compartimento in prateleira:
        for produto in compartimento:
            print(produto, end=' ')
        print()
    print()

# Menus de apps com 3 (ou mais) níveis de profundidade
menu_app = [
    [["Home", "Perfil"], ["Configurações", "Ajuda"]],
    [["Notificações", "Privacidade"], ["Sobre", "Sair"]]
]
print("\nMenu de app:")
for nivel1 in menu_app:
    for nivel2 in nivel1:
        for item in nivel2:
            print(item, end=' ')
        print()
    print()