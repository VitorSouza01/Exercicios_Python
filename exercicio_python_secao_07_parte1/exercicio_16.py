"""
16. Faça um programa que leia um vetor de 5 posições para números reais e, depois, um código inteiro. Se o
código for zero, finalize o programa; se for 1, mostre o vetor na ordem direta; se for 2, mostre o vetor
na ordem inversa. Caso o código for diferente de 1 e 2 escreva uma mensagem informando que o código é
inválido.
"""

lp = 0
lst = []

while lp < 5:
    lp += 1
    vlr = int(input("Digite um número real: "))
    lst.append(vlr)

print("\nDigite um dos seguintes códigos;")
print("[0] - Finalize o programa.")
print("[1] - Valor na ordem direta.")
print("[2] - Valor na ordem inversa.")

cdg = int(input("\nDigitr um código; "))

if cdg == 0:
    print("[Programa Finalizado!]")

elif cdg == 1:
    print(lst)

elif cdg == 2:
    if __name__ == '__main__':
        ivs = list(reversed(lst))
        print(ivs)

else:
    print("[!CÓDIGO INVÁLIDO!]")

