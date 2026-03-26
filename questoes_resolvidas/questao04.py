tamanho_do_vetor = 26
lSecreta_Indice = [int] * tamanho_do_vetor
lSecreta_Indice =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
lSecreta_Letras  = tamanho_do_vetor * [str]
lSecreta_Letras = ["''", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
lSecreta = [int] 
def traduzir():
    for Indice in range(len(lSecreta_Indice)):
        for Letras in range(len(lSecreta_Letras)):
            if lSecreta_Indice[Indice] == lSecreta_Letras[Letras]:
                lSecreta = int(input("Digite o número:\t"))
                #if mensagem_de_saida = lSecreta

print(lSecreta_Letras)
print(lSecreta_Indice)
print(lSecreta)
