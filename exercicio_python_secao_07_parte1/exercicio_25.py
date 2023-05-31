"""
25. Faça um programa que preencha um vetor de tamanho 100 com os 100 primeiros naturais que
não são múltiplos de 7 ou que terminam com 7.
"""

vtr = []
i = 1

while len(vtr) < 100:
  if i % 7 != 0 and i % 10 != 7:
    vtr.append(i)
  i += 1

print(vtr)
