"""
16. Faça um programa para corrigir uma prova com 10 questões de múltipla escolha (a, b, c, d ou e), em uma turma com
3 alunos. Cada questão vale 1 ponto. Leia o gabarito, e para cada aluno leia sua matricula (numero inteiro) e suas
respostas. Calcule e escreva: Para cada aluno, escreva sua matrícula, suas respostas, e suas notas. O percentual
de aprovação, assumindo média 7.0.
"""
matriz = [[], [], []]
numero_matricula = []
loop = 1

# Questões
while True:

    for n in range(1, 4):

        numero = int(input(f"Digite o número inteiro da matricula do 'Aluno{n}': "))
        numero_matricula.append(numero)

        while loop < 11:
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

    while loop < 11:
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
acerto = 0

# Comparação
for aluno in range(3):
    for q in range(10):
        if matriz[aluno][q] == matriz_gabarito[q]:
            acerto += 1

    print(f"Aluno{aluno+1} do número da matricula {numero_matricula[aluno]} marcou as seguintes respostas:"
          f"{matriz[aluno]} teve a nota [{acerto}]. O percentual de aprovação foi de: {((acerto/10)*100)}% ")
    acerto = 0

    print("\n")
