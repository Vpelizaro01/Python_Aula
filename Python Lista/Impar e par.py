try:
    numero1=float(input("Digite um dos seus números:")) 
    if numero1 %2 == 0:
        print(f"Seu numero é par:{numero1}")
    else:
        print(f"Seu numero é impar:{numero1}")
except ValueError:
    print("Error")