"""
20. Faça um programa que leia uma matriz 3 x 6 com valores reais.
(a) Imprima a soma de todos os elementos das colunas ímpares.
(b) Imprima a média aritmética dos elementos da segunda e quarta colunas.
(c) Substitua os valores da sexta coluna pela soma dos valores das colunas 1 e 2.
(d) Imprima a  matriz modificada.
"""

# Matriz Principal
matriz = [[], [], []]
[[matriz[i].append(input("Digite um número: ")) for n in range(6)] for i in range(3)]
print("\nMatriz 3x6;"), [print(matriz[n]) for n in range(3)]


# Matriz Impar
matriz_impar = [[], [], []]
matriz_impar_soma = [[], [], []]
for i in range(3):
    for n in range(0, 5, 2):
        matriz_impar[i].append(matriz[i][n])
for m in range(3):
    for o in range(3):
        matriz_impar_soma[m].append(int(matriz_impar[o][m]))


# Matriz Par
matriz_par = [[], [], []]
matriz_par_soma = [[], []]
for a in range(3):
    for b in range(1, 6, 2):
        matriz_par[a].append(matriz[a][b])
for c in range(2):
    for d in range(3):
        matriz_par_soma[c].append(int(matriz_par[d][c]))


# Soma de todos os elementos das colunas ímpares
nova_matriz_impar_soma = []
print(f"\nSoma de todos os elementos das colunas ímpares;")
for p in range(3):
    nova_matriz_impar_soma.append(sum(matriz_impar_soma[p]))
print(nova_matriz_impar_soma)

# Média aritmética dos elementos da segunda e quarta colunas
nova_matriz_par_soma = []
print(f"\nMédia aritmética dos elementos da segunda e quarta colunas;")
for r in range(2):
    nova_matriz_par_soma.append((sum(matriz_par_soma[r])) / 2)
print(nova_matriz_par_soma)


# Substituição da 6° coluna pela soma dos valores das 1º e 2° colunas
matriz_6_coluna = matriz
print(f"\nSubstituição da 6° coluna pela soma dos valores das 1º e 2° colunas")
for e in range(3):
    matriz_6_coluna[e][5] = (int(matriz[e][0]) + int(matriz[e][1]))
print("Matriz Modificada;"), [print(matriz_6_coluna[n]) for n in range(3)]
