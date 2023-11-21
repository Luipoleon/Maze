import random


class Laberinto:
    matriz = []
    inicio = (0, 0)
    destino = (0, 0)
    _filas = 0
    _columnas = 0

    def _generar_laberinto(self, filas, columnas):
        matriz = [[1] * columnas for _ in range(filas)]

        def dentro_limites(fila, columna):
            return 0 <= fila < filas and 0 <= columna < columnas

        def recursive_backtracker(fila, columna):
            matriz[fila][columna] = 0  # Marcar la celda actual como pasillo

            # Definir direcciones posibles: arriba, abajo, izquierda, derecha
            direcciones = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            random.shuffle(direcciones)

            for direccion in direcciones:
                nueva_fila, nueva_columna = fila + 2 * \
                    direccion[0], columna + 2 * direccion[1]

                if dentro_limites(nueva_fila, nueva_columna) and matriz[nueva_fila][nueva_columna] == 1:
                    matriz[nueva_fila - direccion[0]
                           ][nueva_columna - direccion[1]] = 0
                    recursive_backtracker(nueva_fila, nueva_columna)

        # Comenzar desde una posición aleatoria
        inicio_fila = random.randrange(0, filas, 2)
        inicio_columna = random.randrange(0, columnas, 2)
        recursive_backtracker(inicio_fila, inicio_columna)

        return matriz

    def _generar_inicio(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if self.matriz[i][j] == 0:
                    return (i, j)

    def _generar_destino(self):
        # Start from the last row and move backward
        for i in range(len(self.matriz) - 1, -1, -1):
            # Start from the last column and move backward
            for j in range(len(self.matriz[i]) - 1, -1, -1):
                if self.matriz[i][j] == 0:
                    return (i, j)

    def __init__(self, filas, columnas):
        self._filas = filas
        self._columnas = columnas
        self.matriz = self._generar_laberinto(filas, columnas)
        self.inicio = self._generar_inicio()
        self.destino = self._generar_destino()
