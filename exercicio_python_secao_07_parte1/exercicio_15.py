"""
15. Leia um vetor com 20 números inteiros. Escreva os elementos do
vetor eliminado elementos repetidos.
"""

lp = 0
lst = []

while lp < 20:
	lp += 1
	vlr = float(input(f"Digite o {lp}° valor: "))
	lst.append(vlr)

if __name__ == '__main__':
  lst[:] = list(set(lst))

print(f"\nTodos os valores: {lst}")
