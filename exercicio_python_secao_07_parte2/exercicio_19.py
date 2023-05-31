"""
19. Faça um programa que leia uma matriz de 5 linhas e 4 colunas contendo as seguintes informações sobre alunos de uma
disciplina, sendo todas as informações do tipo inteiro:
    * Primeira coluna: número da matrícula (use um inteiro)
    * Segunda coluna: média das provas
    * Terceira coluna: média dos trabalhos
    * Quarta coluna: nota final

Elabora um programa que:
(a) Leia as três primeiras informações de cada aluno.
(b) Calcule a nota final como sendo a soma da média das provas e da média dos tabalhos
(c) Imprima a matrícula do aluno que obteve a maior nota final (assuma que só existe uma maior nota)
(d) Imprima a média aritmética das notas finais.
"""

matriz = [[], [], [], []]

for n in range(1):
    for m in range(4):
        matriz[m].append(int(input(f"\nDigite o número inteiro da matrícula do {m+1}º Aluno: ")))
        matriz[m].append(input(f"Digite a média das provas do {m+1}º Aluno: "))
        matriz[m].append(input(f"Digite a média dos trabalhos do {m+1}º Aluno: "))

nota_maior = 0
aluno_maior = 0
matriz_nota_maior = []

print("\nNotas finais;")

for i in range(4):
    nota_final = int(matriz[i][1]) + int(matriz[i][2])
    matriz[i].append(nota_final)
    matriz_nota_maior.append(nota_final)

    if nota_final > nota_maior:
        nota_maior = nota_final
        aluno_maior = i

    print(f"Nota final do {i+1}º Aluno: {matriz[i][3]}")

print(f"\nO {aluno_maior+1}º Aluno do número de matricula '{matriz[aluno_maior][0]}' obteve a maior nota final: {nota_maior}")

print(f"\nA média aritmética das notas finais é: {(sum(matriz_nota_maior)) / 4} ")
