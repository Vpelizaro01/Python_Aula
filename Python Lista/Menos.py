while True:
    try:
        numero=float(input("Digite o seu numero:"))
        if numero>0:
         print("Seu valor é positivo")
         break 
        else:  
          print("Erro: O número deve ser positivo. Tente novamente.")
    except ValueError:
       print("digite um numero positvo")
 
   
