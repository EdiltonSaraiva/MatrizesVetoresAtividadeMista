tamanho_do_vetor = 8
vetor_numero = [int] * tamanho_do_vetor
soma = 0
valor_pos_1 = 0 
valor_pos_2 = 0
print("\nIndique valores para um vetor de 8 posições.\n")
for i in range(len(vetor_numero)):
    vetor_numero[i] = int(input("Digite o valor \t"))
print("\nVETOR CRIADO COM SUCESSO!\n")
print("\nAgora indique duas posições (de 0 a 7) para somar os valores que elas correspondem.\n")
valor_pos_1 = int(input("Digite a primeira posicao \t"))
valor_pos_2 = int(input("Digite a segunda posicao \t"))
for i in range(len(vetor_numero)):
    if valor_pos_1 == i:
        soma = soma + vetor_numero[i]
    if valor_pos_2 == i:
        soma = soma + vetor_numero[i]
print("\nO SEU VETOR: ", vetor_numero)
print("Posições digitadas: ", valor_pos_1, "e", valor_pos_2)
print("A soma dos valores das posições indicadas: ", soma, "\n")