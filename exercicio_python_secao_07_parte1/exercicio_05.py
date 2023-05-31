"""
05. Leia um vetor de 10 posições. Contar e escrever quantos valores pares
ele possui.
"""

lp1 = 0
lst = []
lst_pr = []

print("-Digite 10 números\n")
while lp1 < 10:
    lp1 += 1
    nmr = int(input(f"{lp1}° número: "))
    lst.append(nmr)

lp2 = 0
nmr_vrf = 0
qtd_pr = 0
nv_lst = []

while lp2 < 10:
    lp2 += 1
    if lst[nmr_vrf] % 2 == 0:
        ult_nmr = lst[nmr_vrf]
        qtd_pr += 1
        nmr_vrf += 1
        nv_lst.append(ult_nmr)
    else:
    	nmr_vrf += 1

print(f"\nLista: {lst}")
print(f"Quantos números pares tem na lista: {qtd_pr}")
print(f"Lista par: {nv_lst}")
