"""
27. Leia 10 números inteiros e armazene em um vetor. Em seguida escreva os elementos que são primos e suas
respectivas posições no vetor.
"""

vtr = []
vtr_prm = []
psc_prm = []

for i in range(10):
    nmr = int(input(f"Digite o {i+1}º número inteiro: "))
    vtr.append(nmr)

    for i in range(2, nmr):
        if nmr % i == 0:
            # Não é primo!
            break

        else:
            # É primo!
            vtr_prm.append(nmr)
            psc_prm.append(vtr.index(nmr))
            break

print(f"\nVetor com valor original: {vtr}")
print(f"Vetor com valor primo: {vtr_prm}\n")

for i in range(len(vtr_prm)):

    print(f"Número primo: {vtr_prm[i]}. Posição do vetor: {psc_prm[i]}.")






