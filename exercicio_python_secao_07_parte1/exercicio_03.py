"""
03. Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das componentes deste
vetor, armazenando o resultado em outro vetor. Os conjuntos tem 10 elementos cada. Imprimir todos os conjuntos.
"""

print("-Digite 10 números reais")

lp = 0
lst = []
lst_qdd = []

while lp < 10:
    lp += 1
    vlr = int(input(f"Dige o {lp}º número: "))
    lst.append(vlr)
    lst_qdd.append(vlr*vlr)

print(f"\nValores do Vetor: {lst}")
print(f"\nValores do quadrado do Vetor: {lst_qdd}")
