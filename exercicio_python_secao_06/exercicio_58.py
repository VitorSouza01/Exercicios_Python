"""
58. Faça um programa que some os números primos existentes entre A e B, onde A e B são números informados
pelo usuário.
"""
print("-Descubra a soma dos números primos que existem entre A e B.")

a = int(input("\n-Digite o valor de A: "))
b = int(input("-Digite o valor de B: "))
soma = 0

for z in range(a, b+1):
    if z > 1:
        for y in range(2, z):
            if(z % y == 0):
                break
        else:
            soma += z

print(f"\n-A soma dos números primos entre {a} e {b} é; [{soma}].")
