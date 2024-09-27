'''

Criado pelo professor Giovani Da Cruz
https://giovanidacruz.com.br

'''

import math

# Função para retornar o valor de PI
def pi():
    return 3.14

# Função principal
def main():
    # Solicita ao usuário que insira o valor do raio da circunferência
    raio = float(input("Qual é o raio da circunferência? "))

    # Calcula a área da circunferência usando a fórmula: área = raio^2 * PI
    area = math.pow(raio, 2.0) * pi()

    # Exibe o resultado da área
    print(f"\nA área da circunferência é: {area}")

if __name__ == "__main__":
    main()