"""
21. Faça um programa que leia duas matrizes 2 x 2 com valores reais. Ofereça ao usuário um menu de opções:

(a) somar as duas matrizes
(b) subtrair a primeira matriz da segunda
(c) adicionar uma constante às duas matrizes
(d) imprimir as matrizes

Nas duas primeiras opções uma terceira matriz 3 x 3 deve ser criada. Na terceira opção  o valor da constante deve ser
lido e o resultado da adição da constante deve ser armazenado no própria matriz.
"""

# 1º Matriz
matriz1 = [[], []]
[[matriz1[i].append(int(input(f"Digite um número inteiro [{i}, {n}] da 1° Matriz: "))) for n in range(2)]
 for i in range(2)]

# 2º Matriz
matriz2 = [[], []]
[[matriz2[i].append(int(input(f"Digite um número inteiro [{i}, {n}] da 2° Matriz: "))) for n in range(2)]
 for i in range(2)]

# Opções
print("\n[MENU DE OPÇÃO]")
print("(a) somar as duas matrizes")
print("(b) subtrair a primeira matriz da segunda")
print("(c) adicionar uma constante às duas matrizes")
print("(d) imprimir as matrizes")
opcao = input("Digite uma opção do menu: ")

if opcao == "a" or opcao == "(a)":

    # Soma das Matrizes
    matriz_nova = [[], [], []]

    for n in range(2):
        for m in range(2):
            soma = (int(matriz1[n][m]) + int(matriz2[n][m]))
            matriz_nova[n].append(soma)
        matriz_nova[n].append(0)
    for o in range(3):
        matriz_nova[2].append(0)

    print("\nMatriz 3x3 - Soma;"), [print(matriz_nova[n]) for n in range(3)]

elif opcao == "b" or opcao == "(b)":

    # Subtração das Matrizes
    matriz_nova_subt = [[], [], []]

    for n in range(2):
        for m in range(2):
            soma = (int(matriz1[n][m]) - int(matriz2[n][m]))
            matriz_nova_subt[n].append(soma)
        matriz_nova_subt[n].append(0)
    for o in range(3):
        matriz_nova_subt[2].append(0)

    print("\nMatriz 3x3 - Subtração;"), [print(matriz_nova_subt[n]) for n in range(3)]

elif opcao == "c" or opcao == "(c)":
    constante = int(input("\nDigite o valor da constante: "))
    posicao_x_matriz1 = int(input("Digite a posição x [x,y] da Constante da 1º Matriz: "))
    posicao_y_matriz1 = int(input("Digite a posição y [x,y] da Constante da 1º Matriz: "))
    posicao_x_matriz2 = int(input("Digite a posição x [x,y] da Constante da 2º Matriz: "))
    posicao_y_matriz2 = int(input("Digite a posição y [x,y] da Constante da 2º Matriz: "))

    matriz1[posicao_x_matriz1][posicao_y_matriz1] = constante
    matriz2[posicao_x_matriz2][posicao_y_matriz2] = constante

    print("\n1° Matriz 2x2;"), [print(matriz1[n]) for n in range(2)]
    print("\n2° Matriz 2x2;"), [print(matriz2[n]) for n in range(2)]

elif opcao == "d" or opcao == "(d)":

    # Imprimir as Matrizes
    print("\n1° Matriz 2x2;"), [print(matriz1[n]) for n in range(2)]
    print("\n2° Matriz 2x2;"), [print(matriz2[n]) for n in range(2)]
