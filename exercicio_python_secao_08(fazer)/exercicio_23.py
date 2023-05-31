"""
23. Escreva uma função que gera um triângulo lateral de altura 2*n-1 n largura.
Por exemplo, a saída para n= 4 seria:
*
**
***
****
***
**
*
"""


def triangulo_lateral(numero):
    for i in range(1, numero+1):
        print("*" * i)

        if i == numero:
            for n in range(numero+1):
                numero -= 1
                print("*" * numero)
    return ""


numero = int(input("Digite um número que irá gerar a largura de um triâmgulo lateral: "))
print(triangulo_lateral(numero))