"""
29. Faça um programa que receba 6 números inteiros e mostre:
    * Os números pares digitados.
    * A soma dos números pares digitados.
    * Os números ímpares digitados.
    * A quantidade de números ímpares digitados
"""

vtr = []
vtr_par = []
vtr_imp = []

for i in range(6):
	nmr = int(input(f"Digite o {i+1}° número inteiro: "))
	vtr.append(nmr)

	# números pares
	if nmr % 2 == 0:
		vtr_par.append(nmr)

	# númeroa ímpares
	else:
		vtr_imp.append(nmr)

# soma dos números pares
sm_par = sum(vtr_par)

# quantidade de números ímpares
qtd_imp = len(vtr_imp)

print(f"\nLista: {vtr}")
print(f"Números pares: {vtr_par}")
print(f"Soma dos números pares : {sm_par}")
print(f"Números ímpares: {vtr_imp}")
print(f"Quantidade de números ímpares: {qtd_imp}")
