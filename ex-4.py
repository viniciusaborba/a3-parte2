# Faça um algoritmo em que o usuário informa todos os parâmetros necessários para formar dois ou mais
# polinômios e executar a divisão entre esses polinômios. Não utilizar bibliotecas e funções prontas
# do python. O uso de recursividade é permitido.

##########################
# Divisão de polinômios. #
##########################

# A divisão não poderá ser realizada se o coeficiente principal do/s polinômio/s divisor/es for 0, pois a
# divisão por zero é indefinida.

# O grau do dividendo não pode ser menor que o grau do/s divisor/es, pois, na divisão de polinômios, caso seja,
# o resultado da divisão vai ser zero e o dividendo vai ser considerado o resto. Porém, obviamente ambos os
# graus do divisor e dividendo podem ser iguais.

# Com isso, se for realizada uma operação com 3 polinomios por exemplo (1 dividendo e 2 divisores) e o
# dividendo seja grau 1, um dos divisores grau 2 e outro divisor de grau 1, o código barra a operação, pois
# um dos polinomios divisores tem grau maior que o dividendo. Não conseguimos fazer com que a operação siga
# apenas com o dividendo e o outro polinomio divisor.

# Certamente o coeficiente do polinomio de 1 grau não pode exceder 2 valores e o de 2 grau não pode exceder
# 3 valores.

def obter_coeficientes(grau, tipo):
    while True:
        polinomio = input(f"Digite os coeficientes do polinômio {tipo} (ex: 1 2 1 para x^2 + 2x + 1): ")
        coeficientes = list(map(float, polinomio.split()))

        # Ajuste para permitir coeficientes menores
        if (grau == 1 and len(coeficientes) > 2) or (grau == 2 and len(coeficientes) > 3):
            print(f"Erro: Um polinômio de grau {grau} deve ter no máximo {grau + 1} coeficientes.")
            continue

        if grau == 1 and len(coeficientes) < 1:
            print("Erro: Um polinômio de grau 1 deve ter pelo menos 1 coeficiente.")
            continue
        if grau == 2 and len(coeficientes) < 2:
            print("Erro: Um polinômio de grau 2 deve ter pelo menos 2 coeficientes.")
            continue

        return coeficientes

def dividir_polinomios(coef_dividendo, coef_divisor):
    resultado = []
    while len(coef_dividendo) - 1 >= len(coef_divisor) - 1:
        coeficiente = coef_dividendo[0] / coef_divisor[0]
        resultado.append(coeficiente)

        temp_divisor = [coeficiente * coef for coef in coef_divisor]
        novo_dividendo = [coef_dividendo[i] - temp_divisor[i] if i < len(temp_divisor) else coef_dividendo[i]
                          for i in range(len(coef_dividendo))]

        while novo_dividendo and novo_dividendo[0] == 0:
            novo_dividendo.pop(0)

        coef_dividendo = novo_dividendo

    return resultado, coef_dividendo

def main():
    while True:
        num_divisores = input("Quantos polinômios divisores você deseja (1 ou mais)? ")
        if not num_divisores.isdigit() or int(num_divisores) < 1:
            print("Erro: Insira um número válido de polinômios divisores (1 ou mais).")
            continue
        num_divisores = int(num_divisores)
        break

    # Obter o dividendo
    while True:
        grau_dividendo = input("Qual o grau do polinômio dividendo (1 ou 2)? ")
        if grau_dividendo not in ['1', '2']:
            print("Grau inválido. O grau deve ser 1 ou 2.")
            continue

        grau_dividendo = int(grau_dividendo)
        coef_dividendo = obter_coeficientes(grau_dividendo, "dividendo")
        break

    # Obter os divisores
    polinomios_divisores = []
    for i in range(num_divisores):
        while True:
            grau_divisor = input(f"Qual o grau do polinômio divisor {i + 1} (1 ou 2)? ")
            if grau_divisor not in ['1', '2']:
                print("Grau inválido. O grau deve ser 1 ou 2.")
                continue

            grau_divisor = int(grau_divisor)
            coef_divisor = obter_coeficientes(grau_divisor, "divisor")

            if coef_divisor[0] == 0:
                print("Erro: O coeficiente principal do polinômio divisor não pode ser zero.")
                continue

            polinomios_divisores.append((grau_divisor, coef_divisor))  # Armazena o grau junto com os coeficientes
            break

    # Verificar se o grau do dividendo é menor que o grau de algum divisor
    for grau_divisor, coef_divisor in polinomios_divisores:
        if grau_dividendo < grau_divisor:
            print(f"Erro: O grau do dividendo ({grau_dividendo}) é menor que o grau do divisor ({grau_divisor}). A divisão não pode ser realizada.")
            return

    # Divisão sequencial
    for _, coef_divisor in polinomios_divisores:
        coef_dividendo, resto = dividir_polinomios(coef_dividendo, coef_divisor)

    # Exibir resultados
    print("Resultado da divisão dos polinômios:")
    if coef_dividendo:
        print("Quociente: ", " + ".join(f"{coef}x^{i}" for i, coef in enumerate(coef_dividendo) if coef != 0))
    else:
        print("Quociente: 0")
    print("Resto: ", " + ".join(f"{coef}x^{i}" for i, coef in enumerate(resto) if coef != 0) or "0")

if __name__ == "__main__":
    main()