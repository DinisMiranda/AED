conteudo_resumo = """
### Resumo Completo: Ficheiros em Python

#### Abertura de Ficheiros
Utiliza-se a função `open()` para abrir ficheiros.  
**Sintaxe:**
ficheiro = open('nome_do_ficheiro', 'modo', encoding='utf-8')  # encoding opcional

| **Modo** | **Descrição**                                                                 |
|----------|-------------------------------------------------------------------------------|
| 'r'      | Apenas leitura (erro se o ficheiro não existir).                             |
| 'w'      | Escrita (cria um ficheiro novo ou apaga o conteúdo existente).               |
| 'a'      | Escrita (acrescenta ao final do ficheiro, cria o ficheiro se não existir).   |
| 'x'      | Criação de ficheiro (erro se o ficheiro já existir).                         |
| 'r+'     | Leitura e escrita (erro se o ficheiro não existir).                          |
| 'w+'     | Leitura e escrita (apaga conteúdo existente ou cria um ficheiro novo).       |
| 'a+'     | Leitura e escrita (acrescenta ao final, cria o ficheiro se não existir).     |
| 'b'      | Modo binário (adicionado a qualquer modo acima, ex: 'rb', 'wb').            |

#### Fecho de Ficheiros
É importante fechar um ficheiro após o uso para evitar erros.  
ficheiro.close()

Ou usa-se o **context manager**, que fecha o ficheiro automaticamente:
with open('nome_do_ficheiro', 'r') as ficheiro:
    conteudo = ficheiro.read()

#### Leitura de Ficheiros de Texto
| **Método**         | **Descrição**                                                                                     |
|---------------------|---------------------------------------------------------------------------------------------------|
| read()             | Lê todo o ficheiro como uma única string.                                                        |
| read(n)            | Lê n caracteres do ficheiro.                                                                     |
| readline()         | Lê uma única linha do ficheiro como string.                                                      |
| readlines()        | Lê todas as linhas do ficheiro e devolve uma lista.                                              |
| Iteração direta    | Iterar linha a linha: for linha in ficheiro: print(linha.strip()).                              |

Exemplo:
with open('exemplo.txt', 'r', encoding='utf-8') as ficheiro:
    linhas = ficheiro.readlines()
    for linha in linhas:
        print(linha.strip())

#### Escrita em Ficheiros de Texto
| **Modo**    | **Descrição**                                      |
|-------------|----------------------------------------------------|
| 'w'         | Cria/reescreve o ficheiro.                        |
| 'a'         | Acrescenta texto ao final do ficheiro.             |
| 'x'         | Cria ficheiro novo (erro se já existir).           |

Exemplo:
with open('exemplo.txt', 'w', encoding='utf-8') as ficheiro:
    ficheiro.write("Primeira linha.\\n")
    ficheiro.write("Segunda linha.")

#### Posicionamento no Ficheiro
| **Método**         | **Descrição**                                                                               |
|---------------------|---------------------------------------------------------------------------------------------|
| seek(pos, from)    | Move o cursor para pos bytes desde from (0: início, 1: posição atual, 2: final).            |
| tell()             | Retorna a posição atual do cursor.                                                         |

Exemplo:
with open('exemplo.txt', 'r+', encoding='utf-8') as ficheiro:
    ficheiro.seek(5)  # Vai para a posição 5 desde o início
    print(ficheiro.read())  # Lê a partir dessa posição

#### Ficheiros Binários
| **Modo** | **Descrição**                        |
|----------|--------------------------------------|
| 'rb'     | Ler ficheiros binários.             |
| 'wb'     | Escrever ficheiros binários.        |

Exemplo:
with open('exemplo.bin', 'wb') as ficheiro:
    ficheiro.write(b'\\x01\\x02\\x03\\x04')

with open('exemplo.bin', 'rb') as ficheiro:
    dados = ficheiro.read()
    print(dados)

#### Leitura e Escrita Avançada
Codificação UTF-8:
with open('exemplo.txt', 'r', encoding='utf-8') as ficheiro:
    texto = ficheiro.read()

#### Casos Práticos
1. Simulação de Dados Aleatórios:
import random
with open('temperaturas.txt', 'w') as ficheiro:
    for _ in range(10):
        temperatura = round(random.uniform(-10, 40), 2)
        ficheiro.write(f"{temperatura}\\n")

2. Cálculo a partir de Ficheiro:
with open('temperaturas.txt', 'r') as ficheiro:
    temperaturas = [float(linha.strip()) for linha in ficheiro]
    media = sum(temperaturas) / len(temperaturas)
    print(f"Média: {media:.2f}°C")
"""

# Escrever o resumo num ficheiro
with open("resumo_ficheiros_python.txt", "w", encoding="utf-8") as ficheiro:
    ficheiro.write(conteudo_resumo)

print("Resumo criado com sucesso no ficheiro 'resumo_ficheiros_python.txt'.")
