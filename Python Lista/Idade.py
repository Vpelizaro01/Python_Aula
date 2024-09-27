try:
    idade=float(input("Digite sua idade:"))
    if idade < 0:
        print("Não existe idade negativa")
    elif idade < 12:
        print("Você é criança")
    elif idade < 18:
        print("Você é adolescente")
    elif idade < 64:
        print ("Você é adulto")
    else:
        print("Você é idoso")
except ValueError:
    print("Adicione um valor correto")

        
