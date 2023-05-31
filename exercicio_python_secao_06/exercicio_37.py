"""
37. Escreve um programa que verifique quais números entre 1000 e 9999 (inclusive) possuem a propriedade
seguinte: a soma dos dois dígitos de mais baixa ordem com os dois dígitos de mais alta ordem elevada ao
quadrado é igual ao próprio número. Por exemplo, para o inteiro 3025, temos que:

30 + 25 = 55

55(2) = 3025
"""
print("-Programa que verifica qual número entre 1000 e 9999, onde a ordem elevada ao quadrado"
      "é igual ao próprio número.\n")

print("Os números são;")
for n in range(1000, 9999):

    vlr1 = str(n)[0:2]
    vlr2 = str(n)[2:4]

    vlr3 = int(vlr1) + int(vlr2)
    vlr4 = vlr3 * vlr3

    if vlr4 == n:
        print(f"{vlr4}")


