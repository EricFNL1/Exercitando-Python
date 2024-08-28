entrada = int(input("Insira um número e descubra o seu Fatorial: ")) 
fatorial = entrada + 1

total = 1

for i in range(1, fatorial, 1):
    resultado = entrada * (i)
    total *= i
    print(total)