#Faça um algoritmo em que o usuário informa todos os parâmetros necessários para formar dois
#ou mais polinômios e executar a multiplicação entre esses polinômios. Não utilizar bibliotecas
#e funções prontas do python. O uso de recursividade é permitido.

################################
# Multiplicação de polinômios. #
################################

n = int(input("Quantos polinômios você deseja multiplicar? "))
polinomos = []

for i in range(n):
    print("Polinômio {i + 1}:")
    polinomio = input("Digite os coeficientes do polinômio separados por espaço (ex: 2 4 0.5 para 0.5x^2 + 4x + 2): ")
    coeficientes = list(map(float, polinomio.split()))
    polinomos.append(coeficientes)


resultado = polinomos[0]


for polinomio in polinomos[1:]:
    grau_resultante = len(resultado) + len(polinomio) - 1
    novo_resultado = [0] * grau_resultante


    for i in range(len(resultado)):
        for j in range(len(polinomio)):
            novo_resultado[i + j] += resultado[i] * polinomio[j]

    resultado = novo_resultado


print("Resultado da multiplicação dos polinômios:")
print(" + ".join(f"{coef}x^{i}" for i, coef in enumerate(resultado) if coef != 0))
