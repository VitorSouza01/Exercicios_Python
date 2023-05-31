""""
48. Faça um programa que some os termos de valor par da sequência de Fbonacci, cujos valores não ultrapassem
quatro milhões.
"""
print("(-Sequência Fibonacci Até 4 Milhões!)")

cdg = True
a = 1
b = 1
nmr = 4000000

print(f"\n-A Sequência Fibonacci de {nmr} é;")
print(f"\n{a}")
print(b)

c = a + b
print(c)

while cdg:

    d = b + c
    b = c
    c = d

    if d < nmr:
        print(d)

    elif d > nmr:
        break
