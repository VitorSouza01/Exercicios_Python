"""
18. Faça um programa que permita ao usuário entrar com uma matriz de 3 x 3 números iteiros. Em seguida, gere um
array unidimensional pela soma dos números de cada coluna da matriz e amostrar na tela esse array.
Por exemplos,a matriz:

5 -8 10
1 2 15
26 10 7

Vai gerar um vetor, onde cada posição é a soma das colunas da matriz. A primeira posição será 5 + 1 + 25, e assim
por diante:

31 4 3
"""

matriz = [[], [], []]

for n in range(3):
    for m in range(3):
        matriz[n].append(int(input(f"Digite o {1}° valor da matriz: ")))

coluna_matriz = [[], [], []]

print("\nSoma de cada coluna;")

for p in range(3):
    for o in range(3):
        coluna_matriz[p].append(matriz[o][p])

for i in range(3):
    print(f"{i}°Coluna: [{sum(coluna_matriz[i])}]")
