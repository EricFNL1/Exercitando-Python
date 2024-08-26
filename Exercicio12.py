valor = int(input("Insira o valor: \n"))
tipo = str(input("Insira o método de pagamento \n Pix, \n Crédito \n Débito,\n dinheiro: \n"))

if tipo == "Crédito" or tipo == "crédito" or tipo == "credito" or tipo == "Credito":
    total = valor + (valor * 0.05)
    print("Conta:", total)
elif tipo == "Pix" :
    total = valor 
    print("Conta:", total)
if tipo == "Débito":
    total = valor
    print("Conta:", total)
elif tipo == "dinheiro":
    total = valor - (valor * 0.10)
    print("Conta com 10 porcento de desconto:", total)