"""
32. Leia dois vetores inteiros X e Y, cada um com 5 elementos (assuma que o usuário não
informa elementos repetidos). Calcule e mostre os vetores resultantes em cada caso abaixo:

    * Soma entre X e Y: soma de cada elemento de X com o elemento da mesma posição em Y.
    * Produto entre X e Y: multiplicação de cada elemento de X com o elemento da mesma
    posição em Y.
    * Diferença entre X e Y: todos os elementos de X que não existem em Y.
    * Interseção entre X e Y: apenas os elementos que aparecem nos dois vetores.
    * União entre X e Y: todos os elementos de X, e todos os elementos de Y.
"""

vtr_x = []
vtr_y = []
vtr_uniao = []

for i in range(5):
    nmr_x = int(input(f"Digite o {i+1}º número inteiro do Vetor X: "))
    vtr_x.append(nmr_x)
    vtr_uniao.append(nmr_x)

print("\n")

for i in range(5):
    nmr_y = int(input(f"Digite o {i+1}º número inteiro do Vetor Y: "))
    vtr_y.append(nmr_y)
    vtr_uniao.append(nmr_y)


# Soma entre X e Y
vtr_soma = []
for i in range(5):
    soma = (vtr_x[i] + vtr_y[i])
    vtr_soma.append(soma)

print(f"\nSoma das posições entre Vetor X e Vetor Y;")
print(vtr_soma)


# Produto entre X e Y
vtr_produto = []
for i in range(5):
    produto = (vtr_x[i] * vtr_y[i])
    vtr_produto.append(produto)

print(f"\nMultiplicação das posições entre Vetor X e Vetor Y;")
print(vtr_produto)


# Diferença entre X e Y
vtr_diferenca = [vtr_x for vtr_x in vtr_x if vtr_x not in vtr_y]
print(f"\nDiferença dos elementos entre Vetor X e Vetor Y;")
print(vtr_diferenca)


# Interseção entre X e Y
intersecao = set()
vtr_uniao_0 = vtr_uniao
valores = []

for vtr_uniao_0 in vtr_uniao_0:
    if vtr_uniao_0 not in valores:
        valores.append(vtr_uniao_0)
    else:
        intersecao.add(vtr_uniao_0)

print(f"\nInterseção dos elementos que aparecem no Vetor X e Vetor Y;")
print(intersecao)


# União entre X e Y
print(f"\nUnião das posições entre Vetor X e Vetor Y;")
print(vtr_uniao)
