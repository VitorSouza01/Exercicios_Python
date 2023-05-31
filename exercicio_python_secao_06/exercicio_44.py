"""
45. Leia um número positivo do usuário, então, calcule e imprima a sequência Fibonacci até
o primeiro número superior ao número lido.
Exemplo: se o usuário informou o número 30, a sequência a ser impressa será 0 1 1 2 3 5 8 13 21 34
"""
print("(Descubra a Sequência Fibonacci!)")
nmr = int(input("-Digite um número positivo inteiro: "))

cdg = True
a = 1
b = 1

print(f"\n-A Sequência Fibonacci de {nmr} é;")
print(f"\n{a}")
print(b)

if nmr > 0:

    c = a + b
    print(c)

    while cdg:

        d = b + c
        b = c
        c = d
        print(d)

        if d > nmr:
            break

else:
    print("\n(O Número Digitado é Invalido!)")
