inicio = 1

entrada = int(input("Insira um número e descubra o seu Fatorial: ")) 
confirmar = int(input("Confirme o valor de entrada: ")) 

teste = confirmar + 1
recebe = 1
atuali = entrada

while inicio != 0:
    reduz = entrada-1
    atuali += -1
    mult = entrada * reduz
    recebe = mult*reduz 
    teste+= -1
    if teste == 0:
        print(recebe)
        break