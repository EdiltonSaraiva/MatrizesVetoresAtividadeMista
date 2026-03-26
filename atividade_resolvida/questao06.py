import random

print()
print("-" * 25)
print("-----CARTELA DE BINGO----")
print("-" * 25)


linhas_bingo = 5
colunas_bingo = 5
cartela_bingo = [int] * linhas_bingo

for linha_indice in range(len(cartela_bingo)):
    cartela_bingo[linha_indice] = [int] * colunas_bingo

numeros_bingo = [int] * 100

for numero in range(len(numeros_bingo)):
    numeros_bingo[numero] = random.randint(0, 99)

numeros_sorteados = [int] * 25

for sorte in range(len(numeros_bingo)):
    numeros_sorteados = random.sample(numeros_bingo, 25) 

contador = 0

for linhas_da_cartela in range(5):
    for colunas_da_cartela in range(5):
        cartela_bingo[linhas_da_cartela][colunas_da_cartela] = numeros_sorteados[contador]
        contador += 1

for linha_de_impressao in cartela_bingo:
    for num in linha_de_impressao:
        print(f"{num:2d}", end = "   ")
    print()
    print()
print()
