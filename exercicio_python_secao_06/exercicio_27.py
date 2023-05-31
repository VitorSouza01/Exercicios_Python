"""
27. Em Matemática, o número harmônico designado por H(n) define-se como sendo a soma da série harmónica:
    H(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n

Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n).
"""
print("[Descubra o valor de H(n)!]")
n = int(input("-Digite um valor inteiro e positivo: "))
i = 1
soma = 0

if n >= 1:
    while i <= n:
        soma = soma + 1/i
        i += 1
    print('A soma dos %d termos da série vale %f' %(n, soma))

else:
    print('Número informado inválido!')
