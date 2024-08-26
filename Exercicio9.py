altura = int(input("Insira sua altura: \n"))
peso = float(input("Insira o seu peso \n"))

IMC =  (peso / (altura*altura) ) *10000

print(IMC)
if IMC <= 18.5:
    print("Abaixo do peso normal")
elif IMC >= 18.6 and IMC <= 24.9:
    print("Peso Normal")
if IMC >= 25.1 and IMC <= 29.9:
    print("Excesso de peso")
elif IMC >= 30 and IMC <= 34.9:
    print("Obesiadade Classe I")
if IMC >= 35 and IMC <= 39.9:
    print("Obesidade Classe II")
elif IMC > 40:
    print("Obesidade Classe III")