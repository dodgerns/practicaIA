import random


def lanzar_dados():
    return random.randint(1, 6), random.randint(1, 6)


def obtener_combinacion_deseada():
    combinacion_deseada = [(1, 2), (2, 1)]
    resultados = []
    probabilidades = {}
    tiros_realizados = 0

    while True:
        dado1, dado2 = lanzar_dados()
        resultado = (dado1, dado2)

        tiros_realizados += 1

        if resultado in resultados:
            probabilidades[resultado] += 1/36
        else:
            resultados.append(resultado)
            probabilidades[resultado] = 1/36

        if resultado in combinacion_deseada:
            break

    print("Resultados y sus probabilidades:")
    for resultado in resultados:
        probabilidad = probabilidades[resultado] / tiros_realizados
        print("Resultado:", resultado, "- Probabilidad:", probabilidad)

    print("\nTiros realizados:", tiros_realizados)


obtener_combinacion_deseada()