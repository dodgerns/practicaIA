import timeit # solo para medir tiempo
import math

class BusquedaAvara:
    def __init__(self):
        self.estadoInicial = Nodo(3, 3, 0, 0, 1)
        self.arbol = [self.estadoInicial]
        self.estadoVisitados = set()
        self.nodosGenerados = 0

    def solucion(self, estado):
        camino = []
        while estado is not None:
            camino.insert(0, estado)
            estado = estado.padre
        return camino

    # heuristica
    def calcularDistancia(self, estado):
        dx = estado.misionerosIzquierda - 0
        dy = estado.canibalesIzquierda - 0
        return math.sqrt(dx**2 + dy**2)

    def busquedaVoraz(self):
        while len(self.arbol) > 0:
            # heurística (distancia euclidiana) se ordena por la distancia
            self.arbol.sort(key=lambda estado: self.calcularDistancia(estado))
            estadoActual = self.arbol.pop(0)
            self.estadoVisitados.add(str(estadoActual))

            if estadoActual.esMeta():
                print("Solucion encontrada!")
                camino = self.solucion(estadoActual)
                for estado in camino:
                    print(estado)
                return

            estados = estadoActual.generarEstados()
            estados = [estado for estado in estados if str(estado) not in self.estadoVisitados]
            self.nodosGenerados += len(estados)
            for estado in estados:
                estado.padre = estadoActual
                estadoActual.hijos.append(estado)
                self.arbol.append(estado)

class Nodo:
    def __init__(self, misionerosIzquierda, canibalesIzquierda, misionerosDerecha, canibalesDerecha, posicionBarco):
        self.hijos = []
        self.misionerosIzquierda = misionerosIzquierda
        self.canibalesIzquierda = canibalesIzquierda
        self.misionerosDerecha = misionerosDerecha
        self.canibalesDerecha = canibalesDerecha
        self.posicionBarco = posicionBarco
        self.padre = None

    def esValido(self):
        if self.misionerosIzquierda < 0 or self.misionerosDerecha < 0 or self.canibalesIzquierda < 0 or self.canibalesDerecha < 0:
            return False
        if self.misionerosIzquierda > 3 or self.misionerosDerecha > 3 or self.canibalesIzquierda > 3 or self.canibalesDerecha > 3:
            return False
        if self.canibalesIzquierda > self.misionerosIzquierda and self.misionerosIzquierda > 0:
            return False
        if self.canibalesDerecha > self.misionerosDerecha and self.misionerosDerecha > 0:
            return False
        return True

    def esMeta(self):
        return self.misionerosIzquierda == 0 and self.canibalesIzquierda == 0

    def generarEstados(self):
        estados = []
        #bote a la izquierda
        if self.posicionBarco == 1:
            estados.append(Nodo(self.misionerosIzquierda - 1, self.canibalesIzquierda, self.misionerosDerecha + 1,
                                    self.canibalesDerecha, 0))
            estados.append(Nodo(self.misionerosIzquierda, self.canibalesIzquierda - 1, self.misionerosDerecha,
                                    self.canibalesDerecha + 1, 0))
            estados.append(Nodo(self.misionerosIzquierda - 1, self.canibalesIzquierda - 1, self.misionerosDerecha + 1,
                                    self.canibalesDerecha + 1, 0))
            estados.append(Nodo(self.misionerosIzquierda - 2, self.canibalesIzquierda, self.misionerosDerecha + 2,
                                    self.canibalesDerecha, 0))
            estados.append(Nodo(self.misionerosIzquierda, self.canibalesIzquierda - 2, self.misionerosDerecha,
                                    self.canibalesDerecha + 2, 0))
        else:
            estados.append(Nodo(self.misionerosIzquierda + 1, self.canibalesIzquierda, self.misionerosDerecha - 1,
                                    self.canibalesDerecha, 1))
            estados.append(Nodo(self.misionerosIzquierda, self.canibalesIzquierda + 1, self.misionerosDerecha,
                                    self.canibalesDerecha - 1, 1))
            estados.append(Nodo(self.misionerosIzquierda + 1, self.canibalesIzquierda + 1, self.misionerosDerecha - 1,
                                    self.canibalesDerecha - 1, 1))
            estados.append(Nodo(self.misionerosIzquierda + 2, self.canibalesIzquierda, self.misionerosDerecha - 2,
                                    self.canibalesDerecha, 1))
            estados.append(Nodo(self.misionerosIzquierda, self.canibalesIzquierda + 2, self.misionerosDerecha,
                                    self.canibalesDerecha - 2, 1))
        return [estado for estado in estados if estado.esValido()] #operador ternario

    def __str__(self):
        posicionBote = "izquierda" if self.posicionBarco==1 else "derecha"
        return f"Misioneros a la izquierda: {self.misionerosIzquierda}, Canibales a la izquierda: {self.canibalesIzquierda}, " \
               f"Misioneros a la derecha  : {self.misionerosDerecha}, Canibales a la derecha  : {self.canibalesDerecha}, " \
               f"Bote a la {posicionBote}"


busqueda = BusquedaAvara()
tiempo = timeit.timeit(busqueda.busquedaVoraz, number=1)
print("Tiempo de ejecución", tiempo) # 0.00044253599935473176
print("Nodos generados: ", busqueda.nodosGenerados)
