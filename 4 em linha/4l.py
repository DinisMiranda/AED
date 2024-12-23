#criar o tabuleiro
tabuleiro = [[" " for x in range(7)] for _ in range(6)]

#mostrar o tabuleiro
def mostrar_tabuleiro():
    for linha in tabuleiro:
        print("|" + "|".join(linha) + "|")
    print(" 0 1 2 3 4 5 6 ")

#inserir peça
def jogar(coluna, simbolo):
    for i in range(5, -1, -1):  #de baixo para cima
        if tabuleiro[i][coluna] == " ":
            tabuleiro[i][coluna] = simbolo
            return True
    return False  #coluna cheia

#verificar vitória horizontal
def verificar_horizontal():
    for linha in tabuleiro:
        for i in range(4):  
            if linha[i] != " " and linha[i] == linha[i+1] == linha[i+2] == linha[i+3]:
                return True
    return False

#verificar vitória vertical
def verificar_vertical():
    for coluna in range(7):
        for linha in range(3):  
            if tabuleiro[linha][coluna] != " " and tabuleiro[linha][coluna] == tabuleiro[linha+1][coluna] == tabuleiro[linha+2][coluna] == tabuleiro[linha+3][coluna]:
                return True
    return False

#verificar vitória diagonal
def verificar_diagonal():
    #diagonais (\)
    for linha in range(3):  
        for coluna in range(4):  
            if tabuleiro[linha][coluna] != " " and tabuleiro[linha][coluna] == tabuleiro[linha+1][coluna+1] == tabuleiro[linha+2][coluna+2] == tabuleiro[linha+3][coluna+3]:
                return True
    #diagonais (/)
    for linha in range(3, 6):  
        for coluna in range(4):  
            if tabuleiro[linha][coluna] != " " and tabuleiro[linha][coluna] == tabuleiro[linha-1][coluna+1] == tabuleiro[linha-2][coluna+2] == tabuleiro[linha-3][coluna+3]:
                return True
    return False

#jogo principal
print("Bem-vindo ao Jogo Quatro em Linha!")
print("Jogador 1 é 'X' e o Jogador 2 é 'O'")
jogador = 1

while True:
    mostrar_tabuleiro()
    simbolo = "X" if jogador == 1 else "O"
    print(f"Vez do Jogador {jogador} ({simbolo})")
    
    try:
        coluna = int(input("Escolha uma coluna (0-6): "))
        if 0 <= coluna <= 6:
            if jogar(coluna, simbolo):
                if verificar_horizontal() or verificar_vertical() or verificar_diagonal():
                    mostrar_tabuleiro()
                    print(f"Jogador {jogador} venceu!")
                    break
            else:
                print("Coluna cheia! Escolha outra.")
        else:
            print("Coluna inválida. Escolha um número entre 0 e 6.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")


    if verificar_horizontal() or verificar_vertical() or verificar_diagonal():
        mostrar_tabuleiro()
        print(f"Jogador {jogador} venceu!")
        break

    jogador = 2 if jogador == 1 else 1 
