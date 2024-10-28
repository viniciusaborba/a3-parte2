#Faça um algoritmo em que o usuário informa todos os parâmetros necessários para
# formar dois ou mais polinômios e executar a divisão entre esses polinômios. Não
# utilizar bibliotecas e funções prontas do python. O uso de recursividade é permitido.

################################
# Divisão de polinômios.       #
################################

n = int(input("Quantos polinômios você deseja dividir? "))
polinomos = []

for i in range(n):
    print("Polinômio {i + 1}:")
    polinomio = input("Digite os coeficientes do polinômio separados por espaço (ex: 2 4 0.5 para 0.5x^2 + 4x + 2): ")
    coeficientes = list(map(float, polinomio.split()))
    polinomos.append(coeficientes)

dividendo = polinomos[0]
divisor = polinomos[1]

resultado = []
grau_divisor = len(divisor) - 1

while len(dividendo) - 1 >= grau_divisor:
    coeficiente = dividendo[0] / divisor[0]
    resultado.append(coeficiente)

    temp_divisor = [coeficiente * coef for coef in divisor]
    
    novo_dividendo = []
    for i in range(len(dividendo)):
        if i < len(temp_divisor):
            novo_dividendo.append(dividendo[i] - temp_divisor[i])
        else:
            novo_dividendo.append(dividendo[i])

    while novo_dividendo and novo_dividendo[0] == 0:
        novo_dividendo.pop(0)

    dividendo = novo_dividendo

print("Resultado da divisão dos polinômios:")
print("Quociente: ", " + ".join("{coef}x^{i}" for i, coef in enumerate(resultado) if coef != 0))
print("Resto: ", " + ".join("{coef}x^{i}" for i, coef in enumerate(dividendo) if coef != 0))

