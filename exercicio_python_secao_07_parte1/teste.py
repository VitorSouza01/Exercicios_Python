# lê os números A e B
a = int(input("Digite o primeiro número (A): "))
b = int(input("Digite o segundo número (B): "))

# cria vetores com os algarismos de A e B
va = [int(d) for d in str(a)][::-1]
vb = [int(d) for d in str(b)][::-1]

# adiciona zeros aos vetores para deixá-los com o mesmo tamanho
while len(va) < len(vb):
    va.append(0)
while len(vb) < len(va):
    vb.append(0)

# realiza a soma dos vetores, algarismo a algarismo
vsoma = []
carry = 0
for i in range(len(va)):
    s = va[i] + vb[i] + carry
    carry = 0
    if s >= 10:
        s -= 10
        carry = 1
    vsoma.append(s)
if carry == 1:
    vsoma.append(1)

# imprime o resultado da soma
print("A soma de", a, "e", b, "é igual a", "".join(str(d) for d in vsoma[::-1]))
