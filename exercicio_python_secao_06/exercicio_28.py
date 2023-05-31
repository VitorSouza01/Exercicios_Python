"""
28. Faça um programa que leia um valor N inteiro e positivo, calcule o mostre o valor E, conforme a fórmula a seguir:
    E = 1 + 1/1! + 1/2! +1/3! + ... + 1/N!
"""
print("Fórmula; E = 1 + 1/1! + 1/2! +1/3! + ... + 1/N")
nmr = int(input("-Digite um número inteiro positivo: "))
i = 1
soma = 0

if nmr >= 1:
    while i <= nmr:
        soma = soma + 1/i
        i += 1
    soma += 1
    print(f"\nO valor conforme a fórmula é: {soma}.")
else:
    print('Número informado inválido!')
