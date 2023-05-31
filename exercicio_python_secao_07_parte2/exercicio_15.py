"""
15. Leia uma matriz 5x10 que se refere de 10 questões de múltipla escolha, referente a 5 alunos. Leia também um vetor
de 10 posições contendo o gabarito de respostas que podem ser a, b, c ou d, Seu programa deverá comparar as respostas
de cada candidato com o gabarito e emitir um vetor denominado resultado, contendo a pontuação correspondente a
cada aluno.
"""

matriz = [[], [], [], [], []]
loop = 1

# Questões
while True:

    for n in range(1, 6):

        while loop < 11:
            questao = str(input(f"Digite a resposta da {loop}° questão do 'Aluno{n}' (a, b, c, ou d): "))
            while True:

                if questao == 'a' or questao == 'b' or questao == 'c' or questao == 'd':
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

    while loop < 11:
        gabarito = input(f"[Gabarito] Resposta da {loop} questão: ")
        while True:

            if gabarito == 'a' or gabarito == 'b' or gabarito == 'c' or gabarito == 'd':
                loop += 1
                matriz_gabarito.append(gabarito)
                break

            else:
                print("[Resposta Inválida] Digite novamente a resposta correspondente!")
                break
    loop = 1
    break

print("\n")
acerto = 0

# Comparação
for aluno in range(5):
    for q in range(10):
        if matriz[aluno][q] == matriz_gabarito[q]:
            acerto += 1

    print(f"Aluno{aluno+1} acertou {acerto} questões")
    acerto = 0

    print("\n")
