"""
40. Elabore um programa que faça leitura de vários números inteiros, até que se digite um número negativo.
O programa tem que retornar o maior e o menor número lido.
"""
print("[Descubra qual número é menor e maior até digitar um número negativo!]\n")
n = 1

nmr = float(input(f"-Digite o valor do {n}° úmero; "))

nmr_maior = nmr
nmr_menor = nmr

if nmr < 0:
    print(f"\nO Maior número digitado foi; {nmr}.")
    print(f"O Menor número digitado foi; {nmr}.")

else:

    vlr = True

    while vlr:

        while n >= 0:
            n += 1
            nmr = float(input(f"-Digite o valor do {n}° número; "))

            if nmr > nmr_maior:
                nmr_maior = nmr

            elif nmr < nmr_menor:
                nmr_menor = nmr

                if nmr < 0:
                    break
        vlr = False

print(f"\nO Maior número digitado foi; {nmr_maior}.")
print(f"O Menor número digitado foi; {nmr_menor}.")
