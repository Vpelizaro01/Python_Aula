soma = 0
while True:
    entrada=input("Digite um valor ou digite sair:")
    if entrada == "sair":
     print (" Adeus, Obrigado")
     break
    try:
       numero=float(entrada)
       soma += numero  
    except ValueError:
     print("Por favor, digite um número válido ou 'sair'.")
print(f"sua {soma}")

