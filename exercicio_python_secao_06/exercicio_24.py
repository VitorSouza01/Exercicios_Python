"""
24. Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número, com exceção
dele próprio. Ex: a soma dos divisores do número 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78.
"""
print("[Descubra a Soma dos Divisores!]")
nmr = int(input("-Digite um valor de um número inteiro: "))
soma = 0

for i in range(1, nmr):
        if nmr % i == 0:
            print(i)
            soma = soma + i

print(f"\nA soma de todos os divisores é; {soma}.")
