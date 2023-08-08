import random
from queue import PriorityQueue

def lanzarDados():
    return random.randint(1, 6), random.randint(1, 6)

#distancia recorrida por los lanzamientos
def heuristica(combinacionActual, combinacionDeseada):
    distancia = 0
    for dado in combinacionActual:
        if dado not in combinacionDeseada:
            distancia += 1
    return distancia

def obtenerCombinacionDeseada():
    combinacionDeseada = [(1, 2), (2, 1)] # meta

    resultados = []
    probabilidades = {}
    tirosRealizados = 0
    buscandoSolucion = True

    colaPrioridad = PriorityQueue()
    colaPrioridad.put((0, [], (0, 0)))  # (prioridad, camino, combinacionActual)

    combinacionesVisitadas = set()  # Almacenar combinaciones visitadas

    while buscandoSolucion and not colaPrioridad.empty():
        _, camino, combinacionActual = colaPrioridad.get()

        if combinacionActual in combinacionDeseada:
            buscandoSolucion = False
            print("¡Combinación deseada encontrada!")
            print("Combinación:", combinacionActual)

        for _ in range(36):
            dado1, dado2 = lanzarDados()
            nuevaCombinacion = (dado1, dado2)
            if nuevaCombinacion not in combinacionesVisitadas:  # Verificar si la combinación ya ha sido visitada
                combinacionesVisitadas.add(nuevaCombinacion)  # Agregar la combinación a las visitadas
                nuevoCamino = camino + [nuevaCombinacion]
                nuevaPrioridad = len(nuevoCamino) + heuristica(nuevaCombinacion, combinacionDeseada)
                colaPrioridad.put((nuevaPrioridad, nuevoCamino, nuevaCombinacion))

                resultados.append(nuevaCombinacion)
                tirosRealizados += 1

                if nuevaCombinacion in probabilidades:
                    probabilidades[nuevaCombinacion] += 1/36
                else:
                    probabilidades[nuevaCombinacion] = 1/36

    print("\nResultados y sus probabilidades:")
    for resultado in resultados:
        probabilidad = probabilidades[resultado] / tirosRealizados
        print("Resultado:", resultado, "- Probabilidad:", probabilidad)

    print("\nTiros realizados:", tirosRealizados)

obtenerCombinacionDeseada()
