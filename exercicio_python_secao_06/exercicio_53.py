"""
53. Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do chamado
Triangulo de Floyd. Para n = 6, temos;

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
"""
print("[Triangulo de Floyd]")

nmr = int(input("\n-Digite um número inteiro;"))

print(f"\n-O Triangulo de Floyd de número {nmr} é;\n")

vlr = 1

for v1 in range(1, nmr + 1):

    for v2 in range(1, v1 + 1):

        print(vlr, end=' ')
        vlr += 1

    print()
