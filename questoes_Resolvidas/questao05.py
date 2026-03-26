def verificar_quadrado_magico(matriz):
    n = len(matriz)
    soma_referencia = sum(matriz[0])

    for linha in matriz:
        if sum(linha) != soma_referencia:
            return False

    for j in range(n):
        soma_coluna = 0
        for i in range(n):
            soma_coluna += matriz[i][j]
        if soma_coluna != soma_referencia:
            return False

    soma_diagonal_p = 0
    for i in range(n):
        soma_diagonal_p += matriz[i][j]
    if soma_diagonal_p != soma_referencia:
        return False

    soma_diagonal_s = 0
    for i in range(n):
        soma_diagonal_s += matriz[i][n - 1 - i]
    if soma_diagonal_s != soma_referencia:
        return False

    return True

matriz_teste = [
    [8, 0, 7], #PARA MUDAR O RESULTADO, TROCA OS NÚMEROS. COMO: (8 -> 9) FAZENDO ISSO, O QUADRADO NÃO IRA SER MAGICO.
    [4, 5, 6], #SE TROCAR DE VOLTA PARA O 8 OU FAZER A MESMA COISA NOS OUTROS NUMEROS, O QUADRADO VOLTARA A SER MAGICO.
    [3, 10, 2],
]
if verificar_quadrado_magico(matriz_teste):
    print("A matriz é um quadrado magico!")
else:
    print("A matriz NÂO È um quadrado magico")
