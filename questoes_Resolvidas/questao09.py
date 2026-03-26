def determinar_jogada(tabuleiro):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                return i,j
tabuleiro_exemplo = [
    [-1, 1, 1],
    [-1, -1, 0],
    [0, 1, 0],
]

jogada = determinar_jogada(tabuleiro_exemplo)

if jogada:
    linha, coluna = jogada
    print(f"Sugestão de proxima jogada: Linha {linha}, Coluna {coluna}")
else:
    print("Não há jogadas possiveis (Empate ou FIm de jogo).")

print("Casas disponiveis (onde tem 0)")
linha = int(input("Em qual linha você quer jogar? (0, 1 ou 2): "))
coluna = int(input("em qual coluna você quer jogar? (0, 1 ou 2): "))

if tabuleiro_exemplo[linha][coluna] == 0:
    tabuleiro_exemplo[linha][coluna] =-1
    print(f"Você jogou na linha {linha}, coluna {coluna}!")
else:
    print("Essa casa ja esta ocupada ou não existe!")
