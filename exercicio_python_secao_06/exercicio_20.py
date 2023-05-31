""""
20. Ler uma sequência de números inteiros e determinar se eles são pares ou não.
Deverá ser informado o número de dados lidos e número de valores pares.
O processo termina quando for digitado o número 1000.
"""

loop1 = 0
loop2 = 0

while True:
    nmr = int(input("-Digite um número inteiro(Se digitar 1000 o códgo será encerrado!)"))
    loop1 += 1
    if (nmr % 2) == 0:
        loop2 += 1

    if nmr != 1000:
        if (nmr % 2) == 0:
            print(f"O número {nmr} é Par.")
        else:
            print(f"O número {nmr} é Ímpar.")

    if nmr == 1000:
        break

print(f"\nNo loop foi lido no total [{loop1}] dados.")
print(f"No loop [{loop2}] valores são pares.")



