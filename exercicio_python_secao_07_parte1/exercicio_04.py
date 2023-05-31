"""
04. Faça um programa que leia um vetor de 8 posições e, em seguida, leia
também dois valores X e Y quaisquer correspondentes a duas posições no
vetor. Ao final seu programa deverá escrever a soma dos valores encontrados
nas respectativas posições X e Y.
"""


lp = 0
lst1 = []
lst2 = []

print("Digite 8 números\n")
while lp < 8:
	lp += 1
	nmr1 = int(input(f"{lp}° número: "))
	lst1.append(nmr1)

lp = 0

print("\nDigite mais 2 números\n")
while lp < 2:
	lp += 1
	nmr2 = int(input(f"{lp}° número: "))
	lst2.append(nmr2)


print(f"\nPrimeira Lista: {lst1}")
print(f"Segunda Lista: {lst2}")

lst_nv = lst1
lst_nv[0] = (lst1[0]+lst2[0])
lst_nv[1] = (lst1[1]+lst2[1])

print(f"Soma das Listas: {lst_nv}")
