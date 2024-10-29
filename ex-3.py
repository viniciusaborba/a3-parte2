#Faça um algoritmo em que o usuário informa todos os parâmetros necessários para formar dois
#ou mais polinômios e executar a multiplicação entre esses polinômios. Não utilizar bibliotecas
#e funções prontas do python. O uso de recursividade é permitido.

################################
# Multiplicação de polinômios. #
################################

n = int(input("Quantos polinômios você deseja multiplicar? "))
polinomios = []

for i in range(n):
    grau = int(input("Qual o grau do polinômio {i + 1} (1 ou 2)? "))
    
    if grau not in [1, 2]:
        print("Grau inválido. Por favor, insira 1 para primeiro grau ou 2 para segundo grau.")
        continue

    if grau == 1:
        # Caso usuário escolha o polinômio de primeiro grau: ax + b
        polinomio = input("Digite os coeficientes do polinômio (ex: 2 3 para 2x + 3): ")
        coeficientes = list(map(float, polinomio.split()))
        if len(coeficientes) != 2:
            print("Erro: Um polinômio de primeiro grau deve ter 2 coeficientes.")
            continue
    else:
        # Caso o usuário escolha o polinômio de segundo grau: ax^2 + bx + c
        polinomio = input("Digite os coeficientes do polinômio (ex: 1 2 1 para x^2 + 2x + 1): ")
        coeficientes = list(map(float, polinomio.split()))
        if len(coeficientes) != 3:
            print("Erro: Um polinômio de segundo grau deve ter 3 coeficientes.")
            continue

    polinomios.append(coeficientes)

resultado = polinomios[0]

for polinomio in polinomios[1:]:
    grau_resultante = len(resultado) + len(polinomio) - 1
    novo_resultado = [0] * grau_resultante

    for i in range(len(resultado)):
        for j in range(len(polinomio)):
            novo_resultado[i + j] += resultado[i] * polinomio[j]

    resultado = novo_resultado

resultado_str = " + ".join(f"{coef}x^{i}" for i, coef in enumerate(resultado) if coef != 0)
print("Resultado da multiplicação dos polinômios:")
print(resultado_str)
