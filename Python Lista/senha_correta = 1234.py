senha_correta = 1234
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    try:
       

        A= int(input("Digite a senha"))
        if A == senha_correta:
          print("Acesso permitido")
          break
        else:
          print("Acesso Negado")
        tentativas += 1 
        print("Acesso Negado.  Insira senha novamente:",max_tentativas - tentativas)
    except ValueError:
       print("Insira um valor valido")



if tentativas == max_tentativas:
   print("Valor maximo atingido")
                       
        

