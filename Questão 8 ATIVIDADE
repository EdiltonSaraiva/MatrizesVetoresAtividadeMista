gabarito = []
print("--- CADASTRO DO GABARITO ---")
for i in range(10):
    resp = input(f"Resposta da questão {i+1} (a,b,c,d,ou e): ").lower()
    gabarito.append(resp)

for aluno_num in range(1,4):
    print(f"\n--- Dados do Aluno {aluno_num} ---")
    matricula = int(input("Numero da matricula: "))

    respostas_aluno = []
    nota = 0

for i in range(10):
    resp_aluno = input(f"Resposta da questão {i+1}: ").lower()
    respostas_aluno.append(resp_aluno)

    if resp_aluno == gabarito[i]:
        nota += 1

        status = "APROVADO" if nota >= 7 else "REPROVADO"
        percentual_acerto = (nota/10) * 100

        print(f"\nMatricula: {matricula}")
        print(f"Respstas: {respostas_aluno}")
        print(f"Nota final: {nota:.1f}")
        print(f"Percentual de acerto: {percentual_acerto}%")
        print(f"Status: {status}")
