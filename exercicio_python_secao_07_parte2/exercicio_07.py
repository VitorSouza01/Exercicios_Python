"""
07. Gerar e imprimir uma matriz de tamanho 10 x 10, onde seus elementos são de forma:
A[i][j] = 2i + 7j - 2 se i < j
A[i][j] = 3i² - 1 se i = j
A[i][j] = 4i³ - 5j² + 1 se i > j
"""

linhas = 10
colunas = 10

matriz = [[0 for j in range(colunas)] for i in range(linhas)]

for i in range(linhas):
    for j in range(colunas):
        if i < j:
            matriz[i][j] = 2*i + 7*j - 2
        elif i == j:
            matriz[i][j] = 3*i**2 - 1
        else:
            matriz[i][j] = 4*i**3 - 5*j**2 + 1


print("Elementos da Matriz 10 x 10;\n")
for i in range(linhas):
    for j in range(colunas):
        print(matriz[i][j], end='\t')
    print()
