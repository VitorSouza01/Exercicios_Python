"""
05. Leia uma matriz 5x5. Leia também um valor X. O programa deverá fazer uma busca desse valor na matriz e, ao final,
escrever a localização (linha e coluna) ou uma mensagem de "não encontrado".
"""
matriz = [[0 for linha in range(5)]
for coluna in range(5)]

for linha in range(5):
    for coluna in range(5):
        matriz[linha][coluna] = int(input(f"Digite um valor para [{linha}, {coluna}]: "))

buscar = int(input("\nDigite um valor para buscar na matriz: "))

print("\nMatriz;")
for linha in matriz:
    print(linha)

encontrado = False
for linha in range(5):
    for coluna in range(5):
        if matriz[linha][coluna] == buscar:
            print(f"\nO valor {buscar} foi encontrado na linha {linha+1} e na coluna {coluna+1}.")
            encontrado = True
            break

    if encontrado:
        break

if not encontrado:
    print("\nO valor não foi encontrado na Matriz!")
