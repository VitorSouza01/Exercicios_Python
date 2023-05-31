"""
26. Faça um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado.
"""
print("-Descubra o primeiro múltiplo de 11, 13 e 17.")
nmr = int(input("Digite um valor de um número inteiro: "))

for n1 in range(nmr, 1000000000):
    if n1 % 11 == 0:
        break

for n2 in range(nmr, 1000000000):
    if n2 % 13 == 0:
        break

for n3 in range(nmr, 1000000000):
    if n3 % 17 == 0:
        break

print(f"\nO primeiro múltiplo de 11 é; [{n1}].")
print(f"O primeiro múltiplo de 13 é; [{n2}].")
print(f"O primeiro múltiplo de 17 é; [{n3}].")
