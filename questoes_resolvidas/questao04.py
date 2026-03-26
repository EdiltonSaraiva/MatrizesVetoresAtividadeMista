def traduzir(lSecreta):
    codigo = "abcdefghijklmnopqrstuvwxyz"

    mensagem_traduzida = ""

    for numero in lSecreta:

        caractere = codigo[numero]
        mensagem_traduzida += caractere

    return mensagem_traduzida

lSecreta = [0,17,19,7,20,17] #TROCA OS NÚMEROS PARA SELECIONAR AS LETRAS (0 até 25)
resultado = traduzir(lSecreta)

print(f"Mensagem secreta: {lSecreta}")
print(f"Tradução: '{resultado}'")
