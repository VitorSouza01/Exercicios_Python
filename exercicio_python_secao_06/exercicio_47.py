"""
47. Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números:

    * adição (opção 1)
    * subtração (opção 2)
    * multiplicação (opção 3)
    * divisão (opção 4)
    * saída (opção 5)

O programa deve possibilitar ao usuário a escolha da operação desejada, a exibiçaõ do resultado e a volta ao menu
de opções. O programa só termina quando for escolhido a opção de saída (opção 5).
"""
import os

cdg = True

while cdg:

    print("\n[Menu de Opções de Cálculo!]")

    print("\n[Opção 1: Adição.          ]")
    print("[Opção 2: Subtração.       ]")
    print("[Opção 3: Multiplicação.   ]")
    print("[Opção 4: Divisão.         ]")
    print("[Opção 5: Saida.           ]")

    opc0 = int(input("\n-Selecione uma das opções: "))

    if opc0 == 1:

        print("\n-Opção 1: Adição | Foi Selecionada!")
        vlr1 = int(input(".Digite o primeiro valor: "))
        vlr2 = int(input(".Digite o segundo valor:"))

        print(f"\n-Adição: {vlr1} + {vlr2} : {vlr1 + vlr2}.")
        ctn = input("Aperta qualquer tecla para continuar...")
        os.system('cls') or None

    elif opc0 == 2:

        print("\n-Opção 2: Subtração | Foi Selecionada!")
        vlr1 = int(input(".Digite o primeiro valor: "))
        vlr2 = int(input(".Digite o segundo valor:"))

        print(f"\n-Adição: {vlr1} - {vlr2} : {vlr1 - vlr2}.")
        ctn = input("Aperta qualquer tecla para continuar...")
        os.system('cls') or None

    elif opc0 == 3:

        print("\n-Opção 3: Multiplicação | Foi Selecionada!")
        vlr1 = int(input(".Digite o primeiro valor: "))
        vlr2 = int(input(".Digite o segundo valor:"))

        print(f"\n-Adição: {vlr1} * {vlr2} : {vlr1 * vlr2}.")
        ctn = input("Aperta qualquer tecla para continuar...")
        os.system('cls') or None

    elif opc0 == 4:

        print("\n-Opção 4: Divisão | Foi Selecionada!")
        vlr1 = int(input(".Digite o primeiro valor: "))
        vlr2 = int(input(".Digite o segundo valor:"))

        print(f"\n-Adição: {vlr1} / {vlr2} : {vlr1 / vlr2}.")
        ctn = input("Aperta qualquer tecla para continuar...")
        os.system('cls') or None

    elif opc0 == 5:

        cdg = False
        os.system('cls') or None

    else:
        print("\n-Opção Inválida! Digite uma Opção Válida!")
        ctn = input("Aperta qualquer tecla para continuar...")
        os.system('cls') or None
