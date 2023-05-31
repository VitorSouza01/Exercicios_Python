"""
41. Faça um programa que calcula a associação em paralelo de dois resistores R1 e R2 fornecidos pelo usuário via
teclado. O programa fica pedindo estes valores e calculando até que o usuário entre com um valor para resistência
igual a zero.

    R = (R1 * R2) / (R1 + R2)
"""
print("[Associação Em Paralelo De Dois Resistores!]")
print("Obs; O código vai ser finalizado ao digitar zero ou um número menor!")

rstr = True

while rstr:
    r1 = float(input("\n-Digite o valor de R1: "))
    r2 = float(input("-Digite o valor de R2: "))

    if r1 > 0 and r2 > 0:
        rr = (r1 * r2) / (r1 + r2)
        print(f"\nA associação em paralelo de dois resistores é; {rr}.")

    elif r1 <= 0 or r2 <= 0:
        rstr = False

print("\n[CÓDIGO FINALIZADO!]")
