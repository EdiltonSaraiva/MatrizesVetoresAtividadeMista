distancias = [
    [0, 15, 30, 5, 12],
    [15, 0, 10, 17, 28],
    [30, 10, 0, 3, 11],
    [5, 17, 3, 0, 80],
    [12, 28, 11, 80, 0],
]

print("--- CONSULTA DE DISTÂNCIA ---")
origem = int(input("Cidade de origem (0-4): "))
destino = int(input("Cidade de destino (0-4): "))

if 0 <= origem < 5 and 0 <= destino <5:
    km = distancias[origem][destino]
    print(f"A distância entre a cidade {origem} e {destino} é de {km} km.")
else:
    print("Cidade invalida!")

print("\n--- CALCULO DE PERCURSO (MAXIMO 6 TRECHOS) ---")
total_km = 0

for i in range(6):
    print(f"\nTrecho {i + 1}:")
    x = int(input(" Origem (linha): "))
    y = int(input(" Destino (coluna): "))

    if 0 <= x < 5 and 0 <= y < 5:
        valor_trecho = distancias[x][y]
        total_km += valor_trecho
        print(f" Distancia do trecho: {valor_trecho} km")
    else:
        print(" Coordenada invalida! trecho ignorado")

    continuar = input("Deseja adicionar mais um trecho? (s\n): ")
    if continuar.lower() != 's':
        break

    print(f"\nO total percorrido foi de: {total_km} km")
