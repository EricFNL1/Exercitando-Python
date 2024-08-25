# Função para ler valores booleanos e verificar se ambos são verdadeiros ou falsos
def verificar_booleanos(valor1, valor2):
    if valor1 and valor2:
        return "Ambos são VERDADEIROS"
    elif not valor1 and not valor2:
        return "Ambos são FALSOS"
    else:
        return "Os valores são diferentes"

# Exemplo de uso
valor1 = bool(int(input("Digite 1 para VERDADEIRO ou 0 para FALSO (primeiro valor): ")))
valor2 = bool(int(input("Digite 1 para VERDADEIRO ou 0 para FALSO (segundo valor): ")))

resultado = verificar_booleanos(valor1, valor2)
print(resultado)