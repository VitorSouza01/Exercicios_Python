"""
14. Faça um programa que leia um vetor de 10 posições e verifique
se existem valores iguais e os escreva na tela.
"""

lp = 0
lst = []

while lp < 10:
	lp += 1
	vlr = float(input(f"Digite o {lp}° valor: "))
	lst.append(vlr)

if __name__ == '__main__':
  dpl = [x for i, x in enumerate(lst) if i != lst.index(x)]

print(f"\nTodos os valores: {lst}")
print(f"Valores iguais: {dpl}")
