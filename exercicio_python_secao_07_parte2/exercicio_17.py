"""
17. Leia uma matriz 10 x 3 com as notas de 10 alunos em 3 provas. Em seguida, escreva o número de alunos cuja pior
nota foi na prova 1, o número de alunos cuja pior nota foi na prova 2, e o número de alunos cuja pior nota foi na
prova 3. Em caso de empare das piores notas de aluno, o critério de desempate é arbitário,mas o aluno deve ser
contabilizado apenas uma vez.
"""
matriz = [[], [], [], [], [], [], [], [], [], []]
loop = 1

# Questões
while True:

    for n in range(1, 11):

        while loop < 4:
            questao = str(input(f"Digite a resposta da {loop}° questão do 'Aluno{n}' (a, b, c, d ou e): "))
            while True:

                if questao == 'a' or questao == 'b' or questao == 'c' or questao == 'd' or questao == 'e':
                    loop += 1
                    matriz[n-1].append(questao)
                    break

                else:
                    print("[Resposta Inválida] Digite novamente a resposta correspondente!")
                    break
        print("\n")
        loop = 1
    break

matriz_gabarito = []

# Gabarito
while True:

    while loop < 4:
        gabarito = input(f"[Gabarito] Resposta da {loop} questão: ")
        while True:

            if gabarito == 'a' or gabarito == 'b' or gabarito == 'c' or gabarito == 'd' or gabarito == 'e':
                loop += 1
                matriz_gabarito.append(gabarito)
                break

            else:
                print("[Resposta Inválida] Digite novamente a resposta correspondente!")
                break
    loop = 1
    break

print("\n")
erro = 0

# Comparação
for prova in range(3):
    print(f"[Prova{prova+1} - Resposta:({matriz_gabarito[prova]}) - Piores Alunos];")
    for q in range(10):
        if matriz[q][prova] != matriz_gabarito[prova]:
            erro += 1
            print(f"Aluno{q+1} resposta: {matriz[q][prova]}")
    print(f"[Total de piores alunos: {erro}]")
    erro = 0

    print("\n")
