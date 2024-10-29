##########################
# Divisão de polinômios. #
##########################

# Primeiro polinômio (dividendo)
while True:
    grau_dividendo = input("Qual o grau do polinômio dividendo (1 ou 2)? ")
    if grau_dividendo not in ['1', '2']:
        print("Grau inválido. O grau deve ser 1 ou 2.")
        continue

    grau_dividendo = int(grau_dividendo)

    if grau_dividendo == 1:
        polinomio_dividendo = input("Digite os coeficientes do polinômio dividendo (ex: 2 3 para 2x + 3): ")
        coef_dividendo = list(map(float, polinomio_dividendo.split()))
        if len(coef_dividendo) != 2:
            print("Erro: Um polinômio de primeiro grau deve ter exatamente 2 coeficientes.")
            continue
    else:
        polinomio_dividendo = input("Digite os coeficientes do polinômio dividendo (ex: 1 2 1 para x^2 + 2x + 1): ")
        coef_dividendo = list(map(float, polinomio_dividendo.split()))
        if len(coef_dividendo) != 3:
            print("Erro: Um polinômio de segundo grau deve ter exatamente 3 coeficientes.")
            continue
    break

# Segundo polinômio (divisor)
while True:
    grau_divisor = input("Qual o grau do polinômio divisor (1 ou 2)? ")
    if grau_divisor not in ['1', '2']:
        print("Grau inválido. O grau deve ser 1 ou 2.")
        continue

    grau_divisor = int(grau_divisor)

    if grau_divisor == 1:
        polinomio_divisor = input("Digite os coeficientes do polinômio divisor (ex: 2 3 para 2x + 3): ")
        coef_divisor = list(map(float, polinomio_divisor.split()))
        if len(coef_divisor) != 2:
            print("Erro: Um polinômio de primeiro grau deve ter exatamente 2 coeficientes.")
            continue
    else:
        polinomio_divisor = input("Digite os coeficientes do polinômio divisor (ex: 1 2 1 para x^2 + 2x + 1): ")
        coef_divisor = list(map(float, polinomio_divisor.split()))
        if len(coef_divisor) != 3:
            print("Erro: Um polinômio de segundo grau deve ter exatamente 3 coeficientes.")
            continue
    break

if grau_divisor >= grau_dividendo:
    print("Erro: O grau do divisor deve ser menor que o grau do dividendo.")
else:
    resultado = []
    while len(coef_dividendo) - 1 >= grau_divisor:
        coeficiente = coef_dividendo[0] / coef_divisor[0]
        resultado.append(coeficiente)

        temp_divisor = [coeficiente * coef for coef in coef_divisor]

        novo_dividendo = []
        for i in range(len(coef_dividendo)):
            if i < len(temp_divisor):
                novo_dividendo.append(coef_dividendo[i] - temp_divisor[i])
            else:
                novo_dividendo.append(coef_dividendo[i])

        while novo_dividendo and novo_dividendo[0] == 0:
            novo_dividendo.pop(0)

        coef_dividendo = novo_dividendo

    print("Resultado da divisão dos polinômios:")
    if resultado:
        print("Quociente: ", " + ".join(f"{coef}x^{i}" for i, coef in enumerate(resultado) if coef != 0))
    else:
        print("Quociente: 0")
    print("Resto: ", " + ".join(f"{coef}x^{i}" for i, coef in enumerate(coef_dividendo) if coef != 0) or "0")
