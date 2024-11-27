# Resumo dos conceitos de decomposição modular, métodos e funções em Python

# Conceito de Função
# Uma função é um bloco de código reutilizável, projetado para executar uma determinada tarefa.
# Para definir uma função, o Python fornece a keyword def. A seguir está a sintaxe para definir uma função:

def nome_da_funcao(parametros_de_entrada):
    """
    Docstring – documentação da função (opcional)
    Args:
        parametros_de_entrada: Descrição dos parâmetros de entrada
    Returns:
        Descrição do valor retornado (se houver)
    """
    # Corpo da função
    pass

# Exemplo de uma função simples que calcula o fatorial de um número
def fatorial(n):
    """
    Calcula o fatorial de um número.
    
    Args:
        n (int): Número inteiro não negativo
    
    Returns:
        int: Fatorial do número fornecido
    """
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

# Exemplo de uso da função fatorial
print(fatorial(5))  # Saída: 120

# Parâmetros com valor por defeito
# Podemos definir valores padrão para os parâmetros de uma função. Se o argumento não for fornecido, o valor padrão será usado.

def saudacao(nome, mensagem="Olá"):
    """
    Exibe uma mensagem de saudação.
    
    Args:
        nome (str): Nome da pessoa
        mensagem (str): Mensagem de saudação (opcional)
    
    Returns:
        None
    """
    print(f"{mensagem}, {nome}!")

# Exemplo de uso da função saudacao
saudacao("João")  # Saída: Olá, João!
saudacao("Maria", "Bom dia")  # Saída: Bom dia, Maria!

# Número de parâmetros de entrada indefinido
# Podemos definir funções que aceitam um número variável de argumentos usando *args e **kwargs.

def soma(*numeros):
    """
    Calcula a soma de uma quantidade variável de números.
    
    Args:
        *numeros: Números a serem somados
    
    Returns:
        int: Soma dos números fornecidos
    """
    return sum(numeros)

# Exemplo de uso da função soma
print(soma(1, 2, 3))  # Saída: 6
print(soma(4, 5, 6, 7))  # Saída: 22

# Função que avalia o nível de esforço com base na frequência cardíaca
def heartRate(fc):
    """
    Avalia o nível de esforço com base na frequência cardíaca.
    
    Args:
        fc (int): Frequência cardíaca
    
    Returns:
        str: Nível de esforço
    """
    if 50 <= fc <= 80:
        return "treino aeróbico"
    elif 80 < fc <= 100:
        return "treino cardiovascular"
    elif 100 < fc <= 120:
        return "treino aeróbico ideal"
    elif 120 < fc <= 140:
        return "treino anaeróbico"
    else:
        return "fora do intervalo"

# Exemplo de uso da função heartRate
print(heartRate(75))   # Saída: treino aeróbico
print(heartRate(110))  # Saída: treino aeróbico ideal

# Função somatório que recebe dois números inteiros e imprime o somatório dos números no intervalo
def somatorio(a, b):
    """
    Imprime o somatório dos números inteiros no intervalo [a, b].
    
    Args:
        a (int): Início do intervalo
        b (int): Fim do intervalo
    
    Returns:
        None
    """
    soma = sum(range(a, b + 1))
    print(f"Somatório de {a} a {b}: {soma}")

# Exemplo de uso da função somatorio
somatorio(1, 5)  # Saída: Somatório de 1 a 5: 15

# Função maior que recebe n números inteiros positivos e devolve o maior desses números
def maior(*numeros):
    """
    Devolve o maior número entre os números fornecidos.
    
    Args:
        *numeros: Números a serem comparados
    
    Returns:
        int: Maior número entre os fornecidos
    """
    return max(numeros)

# Exemplo de uso da função maior
print(maior(1, 2, 3, 4, 5))  # Saída: 5
print(maior(10, 20, 30))     # Saída: 30