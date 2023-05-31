"""
33. Dados N e dois números inteiros positivos, I e J, diferentes de 0, imprimir em ordem crescente os
N primeiros naturais que são múltiplos de I ou de J e ou de ambos.
Exemplo: Para N = 6, I = 2 e J = 3 a saída deverá ser: 0,2,3,4,6,8
"""
print("Descubra a Ordem Crescente dos Múltiplos!")
n = int(input("-Digite um valor inteiro positivo para 'N': "))
i = int(input("-Digite um valor inteiro positivo para 'I' (Múltiplo): "))
print(f"\nOs Múltiplos de {i} são;")

if n > 0 and i > 0:
    for v1 in range(0, n+1, i):
        print(v1, end=", ")
else:
    print("Número digitado é Inválido!")

j = int(input("\n\n-Digite um valor inteiro positivo para 'J' (Múltiplo): "))
print(f"\nOs Múltiplos de {j} são;")

if n > 0 and j > 0:
    for v2 in range(0, n+1, j):
        print(v2, end=", ")
else:
    print("Número digitado é Inválido!")
