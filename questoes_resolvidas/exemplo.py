linha = 5
coluna = 5

matriz = [int] * linha
for linha_indice in range(len(matriz)):
    matriz[linha_indice] = [int] * coluna
print(matriz)

# ler as linhas
for l in range(len(matriz)):
  #ler as colunas
    for c in range(len(matriz[l])):
        matriz[l][c] = int(input("Digite o valor \t"))
        if l ==c: 
            print("Elemento da diagonal principal",
                  matriz[l][c])
print("")
for l in range(len(matriz)):
    print(matriz[l])
print("")
print(matriz)