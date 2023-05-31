"""
16. Faça uma função chamada DesenhaLinha. Ela dele desenhar uma linha na tela usando vários símbolos de igual
(Ex: ======).
A função recebe pot parâmetro quantos sinais de igual serão mostrados.
"""


def desenha_linha(quantidade):

    return '=' * quantidade


quantidade = int(input("Digite a quantidade de igual '=' para formar uma linha: "))

print(desenha_linha(quantidade))