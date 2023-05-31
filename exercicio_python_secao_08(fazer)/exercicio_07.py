"""
07. Faça uma função que receba uma temperatura em graus Celsius e retorne-a convertida em graus Fahrenheit.
A fórmula de conversão é: F = C * (9.0/5.0) + 32.0, sendo F a temperatura em Fahrenheit e C a temperatura em
Celsius.
"""

def converte_temperatura(celsius):
    return f"\nTemperatura em Celsius: {(celsius * (9.0/5.0) + 32.0)}"


celsius = float(input("Digite a temperatura em Fahrenheit: "))

print(converte_temperatura(celsius))
