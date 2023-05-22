import timeit

class Busqueda:
    def __init__(self):
        self.raiz = Nodo(3, 3, 1)
        self.solucion = None
        self.nodosGenerados = 0

    def buscarSolucion(self):
        cola = [(self.raiz, [])]

        while cola:
            estado, camino = cola.pop(0)

            if estado.esEstadoFinal():
                self.solucion = camino
                return

            estadosPosibles = estado.generarSiguientesEstados()
            self.nodosGenerados += len(estadosPosibles)  # Incrementar el contador de nodos generados

            for estadoPosible in estadosPosibles:
                estado.agregarNuevoEstado(estadoPosible)
                cola.append((estadoPosible, camino + [estadoPosible]))


    def imprimirSolucion(self):
        if self.solucion:
            print("Se encontró una solución:")
            self.solucion.insert(0, self.raiz)
            for estado in self.solucion:
                misionerosIzquierda = estado.misionerosLadoIzq
                canibalesIzquierda = estado.canibalesLadoIzq
                posicionBote = 'bote izquierda' if (estado.posicionBote == 1) else 'bote derecha  '
                misionerosDerecha = 3 - misionerosIzquierda
                canibalesDerecha = 3 - canibalesIzquierda
                print(f"{misionerosIzquierda} Misioneros y {canibalesIzquierda} Canibales {posicionBote} {misionerosDerecha} Misioneros y {canibalesDerecha} Canibales")
        else:
            print("No se encontró ninguna solución.")

class Nodo:
    def __init__(self, misionerosLadoIzq, canibalesLadoIzq, posicionBote):
        self.hijos = []
        self.misionerosLadoIzq = misionerosLadoIzq
        self.canibalesLadoIzq = canibalesLadoIzq
        self.posicionBote = posicionBote

    def estadoValido(self):
        misionerosLadoDerecho = 3 - self.misionerosLadoIzq
        canibalesLadoDerecho = 3 - self.canibalesLadoIzq

        if self.misionerosLadoIzq < 0 or self.misionerosLadoIzq > 3 or misionerosLadoDerecho < 0 or misionerosLadoDerecho > 3 or self.canibalesLadoIzq < 0 or self.canibalesLadoIzq > 3 or canibalesLadoDerecho < 0 or canibalesLadoDerecho > 3:
            return False
        
        # Situación no deseada con los caníbales
        if (self.misionerosLadoIzq > 0 and self.misionerosLadoIzq < self.canibalesLadoIzq) or (misionerosLadoDerecho > 0 and misionerosLadoDerecho < canibalesLadoDerecho):
            return False
        return True

    def esEstadoFinal(self):
        return self.misionerosLadoIzq == 0 and self.canibalesLadoIzq == 0 and self.posicionBote == 0

    def agregarNuevoEstado(self, hijo):
        self.hijos.append(hijo)
    
    def generarSiguientesEstados(self):
        boteLadoDerecho = 1 - self.posicionBote
        posiblesMovimientos = []
        
        for numeroMisioneros in range(3):
            for numeroCanibales in range(3):
                if 1 <= numeroMisioneros + numeroCanibales <= 2:
                    if self.posicionBote == 1:
                        nuevoEstado = Nodo(self.misionerosLadoIzq - numeroMisioneros, self.canibalesLadoIzq - numeroCanibales, boteLadoDerecho)
                    else:
                        nuevoEstado = Nodo(self.misionerosLadoIzq + numeroMisioneros, self.canibalesLadoIzq + numeroCanibales, boteLadoDerecho)
                    if nuevoEstado.estadoValido():
                        posiblesMovimientos.append(nuevoEstado)
        return posiblesMovimientos

busqueda = Busqueda()
tiempo = timeit.timeit(busqueda.buscarSolucion, number=1)
busqueda.imprimirSolucion()
print("Nodos generados:", busqueda.nodosGenerados)
print("Tiempo de ejecución:", tiempo)
