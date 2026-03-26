vetor = []

print("Digite os valores do vetor:")
for i in range(8):
    valor = float(input(f"Posição {i}: "))
    vetor.append(valor)

print("\nAgora escolha duas posições (de 0 a 7) para somar seus valores.")
x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

if 0 <= x < 8 and 0 <= y < 8:
    soma = vetor[x] + vetor[y]
    print(f"\nA soma dos valores nas posições {x} e {y} é: {soma}")
else:
    print("\nErro: uma ou ambas as ambas posições digitadas são inválidas!")
