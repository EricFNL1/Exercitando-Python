inicio = 0
positivos = 0

while inicio != 11:
    num = int(input("Insira um número: "))
    inicio+=1
    teste = num % 2
    if teste == 0:
        positivos +=1
    if inicio == 10:
        print("Dos 10 Números inseridos, somente", positivos,"São positivos.")
        break
        
        
