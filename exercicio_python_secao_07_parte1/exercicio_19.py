"""
19. Faça um vetor de tamanho 50 preenchido com o seguinte valor: (i+5*i)%(i+1), sendo i a posição do elemento
no vetor. Em seguida imprima o vetor na tela.
"""

import numpy as np

vetor = np.zeros(50)

for i in range(len(vetor)):
    vetor[i] = (i + 5 *i) % (i +1)

print(f"Valor do Vetor: {vetor}")
