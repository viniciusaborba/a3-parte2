def criar_polinomio():
    grau = int(input("Informe o grau do polinômio: "))
    coeficientes = []
    for i in range(grau + 1):
        coef = int(input(f"Informe o coeficiente para x^{grau - i}: "))
        coeficientes.append(coef)
    return coeficientes

def somar_polinomios(polinomio1, polinomio2):
    while len(polinomio1) < len(polinomio2):
        polinomio1.insert(0, 0)
    while len(polinomio2) < len(polinomio1):
        polinomio2.insert(0, 0)

    def soma_recursiva(p1, p2, index=0):
        if index == len(p1):
            return []
        else:
            return [p1[index] + p2[index]] + soma_recursiva(p1, p2, index + 1)

    return soma_recursiva(polinomio1, polinomio2)

def exibir_polinomio(polinomio):
    termos = []
    grau = len(polinomio) - 1
    for i, coef in enumerate(polinomio):
        if coef != 0:
            termo = f"{coef}x^{grau - i}" if grau - i > 0 else f"{coef}"
            termos.append(termo)
    return " + ".join(termos)

def main():
    num_polinomios = int(input("Informe o número de polinômios para somar: "))
    polinomios = []

    for i in range(num_polinomios):
        print(f"\nDefina os coeficientes do polinômio {i + 1}:")
        polinomios.append(criar_polinomio())

    resultado = polinomios[0]
    for i in range(1, num_polinomios):
        resultado = somar_polinomios(resultado, polinomios[i])

    print("\nPolinômio resultante da soma:")
    print(exibir_polinomio(resultado))

main()
