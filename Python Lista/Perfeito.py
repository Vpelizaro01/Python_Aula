def Número_perfeito(Número):
    sum=0

    
    for i in range(1, Número):
        if Número % i == 0:
            sum += i

    if sum == Número:
        return True
    else:
        return False

Número = int(input("Digite um número: "))


if Número_perfeito(Número):
    print(Número, "é um número perfeito.")
else:
    print(Número, "não é um número perfeito.")