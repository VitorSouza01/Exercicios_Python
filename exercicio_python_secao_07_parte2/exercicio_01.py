"""
01. Leia uma matriz 4x4, conte e escreva quantos valores maiores que 10 ela possui.
"""

# numero = int(input("Digite o tamanho da matriz: "))

numero = 4
linha = [0] * numero
matriz = [linha] * numero
print(f"Matriz 4x4: {matriz}.\n")

for i in range(numero):
    linha = []
    for c in range(numero):
        numero_novo = int(input(f"Digite o número que ficara armazenado {i},{c}:"))
        linha.append(numero_novo)
    matriz[i] = linha

maior_que_10 = 0
for linha in matriz:
    for valor in linha:
        if valor > 10:
            maior_que_10 += 1


print("\nMatriz Atualizada;")
for linha in matriz:
    print(linha)

print(f"\nQuantos valores maior que 10 tem na matriz: {maior_que_10}.")
