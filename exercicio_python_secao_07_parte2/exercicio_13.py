"""
13. Gere matriz 4 x 4 com valores no intervalo [1, 20]. Escreva um programa que transforme a matriz gerada numa matriz
triangular inferior, ou seja, atribuido zero a todos os elementos acima da diagonal principal. Imprima a matriz
original e a matriz transformada.
"""

valor = 1
matriz = []

for n in range(4):
    linha = []

    for m in range(4):
        linha.append(valor)
        valor += 1
    matriz.append(linha)

print("Matriz original 4x4;")
for linha in matriz:
    print(linha)

for i in range(3):
    i += 1
    matriz[0][-i] = 0

for j in range(2):
    j += 1
    matriz[1][-j] = 0

for k in range(1):
    k += 1
    matriz[2][-k] = 0

print("\nMatriz 4x4 transformada em triangular inferior;")
for linha in matriz:
    print(linha)
