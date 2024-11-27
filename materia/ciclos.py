# Exemplo 1: Maior número e média dos 10 números fornecidos

# Inicializa as variáveis
maior_numero = float('-inf')  # O maior número começa com um valor muito baixo
soma = 0                      # Soma dos números válidos
contador = 0                  # Contador de números válidos

# Loop para ler 10 números do usuário
for i in range(10):
    numero = int(input(f"Digite o número {i+1}: "))  # Solicita um número ao usuário
    
    # Se o número for maior que 20, ignora e vai para o próximo número
    if numero > 20:
        continue  # O continue faz com que o código pule para a próxima iteração do loop
    
    # Soma o número e conta os números válidos
    soma += numero
    contador += 1
    
    # Verifica se o número é maior que o atual maior número
    if numero > maior_numero:
        maior_numero = numero

# Calcula a média, se houver números válidos
if contador > 0:
    media = soma / contador  # Média dos números válidos
    print(f"O maior número é: {maior_numero}")  # Exibe o maior número
    print(f"A média dos números válidos é: {media}")  # Exibe a média
else:
    print("Nenhum número válido foi inserido.")  # Caso não haja números válidos


# Exemplo 2: Função Fatorial

# Função para calcular o fatorial de um número
def calcular_fatorial(n):
    if n == 0:  # O fatorial de 0 é 1
        return 1
    
    fatorial = 1  # Inicializa o valor do fatorial
    for i in range(1, n + 1):  # Loop para multiplicar os números de 1 até n
        fatorial *= i  # Multiplica o número atual ao fatorial
    
    return fatorial  # Retorna o resultado do fatorial

# Solicita ao usuário um número para calcular o fatorial
numero = int(input("Digite um número para calcular o fatorial: "))

# Chama a função e exibe o resultado
resultado = calcular_fatorial(numero)  # Chama a função para calcular o fatorial
print(f"O fatorial de {numero} é {resultado}")  # Exibe o resultado do fatorial
