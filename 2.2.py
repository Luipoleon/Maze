from queue import Queue
import time
import os
from laberinto import Laberinto

from colorama import init, Fore, Back, Style


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def slow_print(matriz_laberinto, camino, speed):
    imprimir_laberinto(matriz_laberinto, camino)
    time.sleep(speed)

# Función para imprimir el laberinto


def imprimir_laberinto(matriz_laberinto, camino=None):
    print()
    print("⬜" * (len(matriz_laberinto[0]) + 2))
    for i in range(len(matriz_laberinto)):
        print("⬜", end="")
        for j in range(len(matriz_laberinto[0])):
            if (i, j) == inicio:
                print("🔴", end="")
            elif (i, j) == destino:
                print("🌟", end="")
            elif camino and (i, j) in camino:
                print("◽", end="")
            elif matriz_laberinto[i][j] == 1:
                print("🔳", end="")
            else:
                print("  ", end="")
        print("⬜", end="\n")
    print("⬜" * (len(matriz_laberinto[0]) + 2))
    print()

# Implementación de BFS


def bfs(matriz_laberinto, inicio, destino, slow=False, speed=0.2):
    queue = Queue()
    queue.put([inicio])

    while not queue.empty():
        camino = queue.get()
        actual = camino[-1]

        if actual == destino:
            imprimir_laberinto(matriz_laberinto, camino)
            return camino

        if (slow):
            slow_print(matriz_laberinto, camino, speed)

        for vecino in obtener_vecinos(matriz_laberinto, actual):
            if vecino not in camino:
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                queue.put(nuevo_camino)


# Implementación de DFS


def dfs(matriz_laberinto, inicio, destino, camino=None, slow=False, speed=0.2):
    if camino is None:
        camino = []

    camino = camino + [inicio]

    if inicio == destino:
        imprimir_laberinto(matriz_laberinto, camino)
        return camino

    if (slow):
        slow_print(matriz_laberinto, camino, speed)

    for vecino in obtener_vecinos(matriz_laberinto, inicio):
        if vecino not in camino:
            nuevo_camino = dfs(matriz_laberinto, vecino,
                               destino, camino, slow, speed)
            if nuevo_camino:
                return nuevo_camino

    return None

# Función para obtener los vecinos válidos


def obtener_vecinos(matriz_laberinto, actual):
    filas, columnas = len(matriz_laberinto), len(matriz_laberinto[0])
    # Derecha, Izquierda, Abajo, Arriba
    movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    vecinos = [(actual[0] + dy, actual[1] + dx) for dy, dx in movimientos]
    vecinos = [(i, j) for i, j in vecinos if 0 <= i <
               filas and 0 <= j < columnas and matriz_laberinto[i][j] == 0]

    return vecinos


# VARIABLES GLOBALES
# Define el laberinto (0 para espacios libres, 1 para obstáculos)
filas = 0
columnas = 0
laberinto = None
slow = False
matriz_laberinto = []

# Define el punto de inicio y el punto de destino
inicio = (0, 0)
destino = (0, 0)


def imprimir_menu_principal():
    print("********************************")
    print("        MENÚ PRINCIPAL")
    print("********************************")
    print(" 1. BFS")
    print(" 2. DFS")
    print(" 3. Salir\n")


def get_values(titulo):

    global filas, columnas, laberinto, matriz_laberinto, inicio, destino, slow
    slowInput = ""
    clear_screen()
    print("********************************")
    print(f" GENERA TU LABERINTO {titulo}  ")
    print("********************************")

    try:
        filas = int(input(" Filas: "))
        columnas = int(input(" Columnas: "))
        slowInput = input(" Lento(y): ")

    except:
        print("\n ¡Valores inválidos!")
        input(" (Presione ENTER para continuar)")
        get_values(titulo)

    slow = True if slowInput == 'y' else False

    laberinto = Laberinto(filas, columnas)
    matriz_laberinto = laberinto.matriz
    inicio = laberinto.inicio
    destino = laberinto.destino


def main():
    # Encuentra el camino usando BFS y DFS
    opcion = "0"
    while (opcion != "3"):
        clear_screen()
        imprimir_menu_principal()
        opcion = input(" Elige una opción: ")
        if (opcion == "1"):
            get_values("BFS")
            bfs(matriz_laberinto, inicio, destino, slow)

        elif (opcion == "2"):
            get_values("DFS")
            dfs(matriz_laberinto, inicio, destino, None, slow)

        elif (opcion == "3"):
            print("\n ¡Hasta pronto!")
        else:
            print("\n ¡Elija una opción válida!")
        input(" (Presione ENTER para continuar)")


if __name__ == "__main__":
    # # Inicializar colorama
    # init()
    # # Definir colores
    # color_fondo = Back.BLACK  # Fondo morado
    # color_letras = Fore.WHITE    # Letras blancas
    # print(color_fondo + color_letras)
    main()
