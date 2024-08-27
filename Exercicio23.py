hora = int(input("Insira o valor da hora aula: "))
aulas = int(input("Insira a quantidade de aulas: "))

salariobruto = hora * aulas

if  salariobruto <= 1045:
    salarioliquido = salariobruto - (salariobruto * 0.075)
    print("O sálario é:", salarioliquido)
elif salariobruto > 1045 and salariobruto <= 2089.60:
    salarioliquido = salariobruto - (salariobruto * 0.09)
    print("O sálario é:", salarioliquido)
if salariobruto > 2089.60 and salariobruto <= 3134.40:
    salarioliquido = salariobruto - (salariobruto * 0.12)
    print("O sálario é:", salarioliquido)
elif salariobruto > 3134.40 and salariobruto < 6101.06:
    salarioliquido = salariobruto - (salariobruto * 0.14)
    print("O sálario é:", salarioliquido)
