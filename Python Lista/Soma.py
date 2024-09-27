try:
     numero1=float(input("Digite um dos seus números:")) 
     numero2=float(input("Digite o segundo valor:"))
     resultado = numero1 + numero2
     print(f"Esse é o seu:{resultado}")
except ValueError:
     print("Digite um valor correto")
     
