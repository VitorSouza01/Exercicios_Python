"""
57. Faça um programa que conte quanto números primos existem entre A e B, onde A e B são números informados pelo
usuário.
"""
print("-Descubra quantos números primos existem entre A e B.")
a = int(input("\n-Digite o valor de A: "))
b = int(input("-Digite o valor de B: "))
vzs = 0

for z in range(a, b+1):
    if z > 1:
        for y in range(2, z):
            if(z % y == 0):
                break
        else:
            vzs += 1
            print(z)

print(f"\n-Entre {a} e {b} existe [{vzs}] números primos.")
