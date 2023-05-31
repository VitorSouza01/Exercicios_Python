"""
30. Faça programas para calcular as seguintes sequências:
    1 + 2 + 3 + 4 + 5 + ... + n
    1 - 2 + 3 - 4 + 5 + ... + (2n - 1)
    1 + 3 + 5 + 7 + ... (2n - 1)
"""
print("OPERAÇÃO;")
print("A) 1 + 2 + 3 + 4 + 5 + ... + n")
print("B) 1 - 2 + 3 - 4 + 5 + ... + (2n - 1)")
print("C) 1 + 3 + 5 + 7 + ... (2n - 1)")

numero = int(input("\nDigite um número: "))

# A)---

resultado = 1
for n in range(1, numero + 1):
    resultado += n

# B)---

subtracao = 0
divisao = numero % 2

if divisao == 0:
    subtracao = divisao - (numero/2)
    resultado2 = int(subtracao)

else:
    divisao2 = numero / 2
    soma = divisao2 + 0.5
    resultado2 = int(soma)

# C)---

total = 0

for i in range(1, numero + 1, 2):
    total += i
#   print(i, total)


print("\nRESULTADOS;")
print(f"A){resultado}")
print(f"B){resultado2}")
print(f"C){total}")
