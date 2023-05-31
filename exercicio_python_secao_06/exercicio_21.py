""""
21. Faça um programa que receba dois números. Calcule e mostre:
    * A soma dos números pares desse intervalo de números, incluindo os números digitados.
    * A multiplicação dos números ímpares desse intervalor, incluindo os digitados;
"""
print("DIGITE OS NÚMEROS EM ORDEM CRESCENTE")
nmr1 = int(input("-Digite o primeiro valor: "))
nmr2 = int(input("-Digite o segundo valor: "))
soma = 0
multiplicacao = 0

# se o valor inicial for par
if (nmr1 % 2) == 0:

    # soma_par
    for n in range(nmr1+2, nmr2, 2):
        print(n)
        soma = soma + n
    soma = soma + nmr1 + nmr2
    print(f"[A soma dos intervalos dos números pares incluindo os números digitados são: {soma}.]\n")

    # multiplicacao_impar
    for n in range(nmr1+1, nmr2, 2):
        print(n)
        multiplicacao = multiplicacao + n
    multiplicacao = multiplicacao + nmr1 + nmr2
    print(f"[A soma dos intervalos dos números ímpares incluindo os números digitados são: {multiplicacao}.]")

# se o valor inicial for ímpar
else:

    # soma_par
    for n in range(nmr1 + 1, nmr2, 2):
        print(n)
        soma = soma + n
    soma = soma + nmr1 + nmr2
    print(f"[A soma dos intervalos dos números pares incluindo os números digitados são: {soma}.]\n")

    # multiplicacao_impar
    for n in range(nmr1 + 2, nmr2, 2):
        print(n)
        multiplicacao = multiplicacao + n
    multiplicacao = multiplicacao + nmr1 + nmr2
    print(f"[A soma dos intervalos dos números ímpares incluindo os números digitados são: {multiplicacao}.]")
