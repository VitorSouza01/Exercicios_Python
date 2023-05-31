"""
04. Leia uma matriz 4x4, imprima a matriz e retorne a localização (linha e a coluna) do maior valor.
"""

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for linha in range(0, 4):
    for coluna in range(0, 4):
        matriz[linha][coluna] = int(input(f"Digite um valor para [{linha}, {coluna}]: "))

print("\nMatriz 4x4;")
for linha in range(0, 4):
    for coluna in range(0, 4):
        print(f"[{matriz[linha][coluna]}]", end="")
    print()

print("\nLinha e coluna do maior valor da matriz;")
print(max(matriz))
