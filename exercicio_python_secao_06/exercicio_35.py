"""
35. Faça um programa que some os números impares contidos em um intervalo definido pelo usuário.
O usuário define o valor inicial do intervalo e o valor final deste intervalo e o programa deve somar
todos os números ímpares contidos neste intervalo. Caso o usuário digite um intervalo inválido
(começando por um valor maior que o valor final) deve ser escrito uma mensagem de erro na tela,
"Intervalo de valores inválido" e o programa termina.

Exemplo da tela de saída: Digite o valor inicial e valor final: 5 e 10
Soma dos ímpares neste intervalo: 21
"""
print("[Descubra a soma de todos os números ímpares contido no intervalo de 2 números!]")
vlr1 = int(input("-Digite o valor inicial: "))
vlr2 = int(input("-Digite o valor final: "))

sm1 = 0
sm2 = 0

if vlr1 < vlr2:

    if vlr1 % 2 == 0:
        for n in range(vlr1+1, vlr2+1, 2):
            sm1 = sm1 + n
        print(f"\n-Soma dos ímpares neste intervalo: {sm1}.")

    else:
        for n in range(vlr1, vlr2+1, 2):
            sm2 = sm2 + n
        print(f"\n-Soma dos ímpares neste intervalo: {sm2}.")

else:
    print("\n[Erro! Intervalo de Valores Inválido!]")
