while True:
    try:
        numero= float(input("Digite o seu valor:"))
        if numero <0:
            print("Erro: O número deve ser um inteiro positivo. Tente novamente.")
        else:
            fatorial = 1 if numero == 0 else 1
        if numero > 0:
            fatorial=1
        n= numero
        while n>1: 
              fatorial *= n
              n -=1
        print(f"O fatorial de {numero} é {fatorial}")
        break
    except ValueError:
        print("Insira um número inteiro corretamente")