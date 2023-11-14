#Héctor Sebastián Garrido López 1102123
print("Proyecto #2")
# Función para inicializar un tablero vacío de 10x10
def inicializar_tablero():
    tablero = []
    for _ in range(10):
        fila = ["."] * 10  # "." representa casilla vacía
        tablero.append(fila)
    return tablero

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    print("  1 2 3 4 5 6 7 8 9 10")
    for i, fila in enumerate(tablero):
        fila_str = " ".join(fila)
        print(chr(65 + i) + " " + fila_str)

# Función para verificar si una coordenada está dentro del tablero
def dentro_del_tablero(fila, columna):
    return 0 <= fila < 10 and 0 <= columna < 10

# Función para colocar un barco en el tablero
def colocar_barco(tablero, fila, columna, orientacion, longitud):
    if orientacion == "horizontal":
        for i in range(longitud):
            if not dentro_del_tablero(fila, columna + i) or tablero[fila][columna + i] != ".":
                return False
        for i in range(longitud):
            tablero[fila][columna + i] = "B"  # "B" representa un barco
    else:  # orientacion vertical
        for i in range(longitud):
            if not dentro_del_tablero(fila + i, columna) or tablero[fila + i][columna] != ".":
                return False
        for i in range(longitud):
            tablero[fila + i][columna] = "B"
    return True

# Función para realizar un disparo en el tablero del oponente
def disparar(tablero, fila, columna):
    if tablero[fila][columna] == "B":
        tablero[fila][columna] = "X"  # "X" representa un disparo exitoso
        return "¡Has golpeado un barco!"
    elif tablero[fila][columna] == ".":
        tablero[fila][columna] = "-"  # "-" representa un disparo fallido
        return "Agua"
    else:
        return "Ya habías disparado aquí antes."

# Función para verificar si un jugador ha perdido
def jugador_perdio(tablero):
    for fila in tablero:
        if "B" in fila:
            return False
    return True

def obtener_fila():
    while True:
        entrada = input("Fila (A-J): ").strip().lower()
        if entrada.isalpha() and len(entrada) == 1 and 'a' <= entrada <= 'j':
            return ord(entrada) - ord('a')
        else:
            print("Entrada inválida. Inténtalo de nuevo.")

def obtener_columna():
    while True:
        entrada = input("Columna (1-10): ").strip()
        if entrada.isdigit() and 1 <= int(entrada) <= 10:
            return int(entrada) - 1
        else:
            print("Entrada inválida. Inténtalo de nuevo.")

def obtener_orientacion():
    while True:
        entrada = input("Orientación (horizontal/vertical): ").strip().lower()
        if entrada == "horizontal" or entrada == "vertical":
            return entrada
        else:
            print("Entrada inválida. Inténtalo de nuevo.")

# Función principal del juego
def juego_de_battleship():
    print("¡Bienvenido al juego de Battleship!")

    # Inicializar tableros para los dos jugadores
    tablero_jugador1 = inicializar_tablero()
    tablero_jugador2 = inicializar_tablero()

    # Colocar barcos para el jugador 1
    barcos_colocados_jugador1 = 0
    # Barcos pequeños (3 casillas)
    while barcos_colocados_jugador1 < 3:
        print("Jugador 1, coloca un barco pequeño (3 casillas):")
        fila = obtener_fila()
        columna = obtener_columna()
        orientacion = obtener_orientacion()

        if colocar_barco(tablero_jugador1, fila, columna, orientacion, 3):
            barcos_colocados_jugador1 += 1
        else:
            print("No se pudo colocar el barco en esa ubicación. Inténtalo de nuevo.")
        imprimir_tablero(tablero_jugador1)

    # Barcos grandes (5 casillas)
    barcos_colocados_jugador1 = 0
    while barcos_colocados_jugador1 < 2:
        print("Jugador 1, coloca un barco grande (5 casillas):")
        fila = obtener_fila()
        columna = obtener_columna()
        orientacion = obtener_orientacion()

        if colocar_barco(tablero_jugador1, fila, columna, orientacion, 5):
            barcos_colocados_jugador1 += 1
        else:
            print("No se pudo colocar el barco en esa ubicación. Inténtalo de nuevo.")
        imprimir_tablero(tablero_jugador1)


    # Colocar barcos para el jugador 2
    barcos_colocados_jugador2 = 0

    # Barcos pequeños (3 casillas)
    while barcos_colocados_jugador2 < 3:
        print("Jugador 2, coloca un barco pequeño (3 casillas):")
        fila = obtener_fila()
        columna = obtener_columna()
        orientacion = obtener_orientacion()

        if colocar_barco(tablero_jugador2, fila, columna, orientacion, 3):
            barcos_colocados_jugador2 += 1
        else:
            print("No se pudo colocar el barco en esa ubicación. Inténtalo de nuevo.")
        imprimir_tablero(tablero_jugador2)

    # Barcos grandes (5 casillas)
    barcos_colocados_jugador2 = 0
    while barcos_colocados_jugador2 < 2:
        print("Jugador 2, coloca un barco grande (5 casillas):")
        fila = obtener_fila()
        columna = obtener_columna()
        orientacion = obtener_orientacion()

        if colocar_barco(tablero_jugador2, fila, columna, orientacion, 5):
            barcos_colocados_jugador2 += 1
        else:
            print("No se pudo colocar el barco en esa ubicación. Inténtalo de nuevo.")
        imprimir_tablero(tablero_jugador2)

    # Juego principal
    turno = 1
    while True:
        if turno == 1:
            print("Turno del Jugador 1")
            imprimir_tablero(tablero_jugador1)
            fila = obtener_fila()
            columna = obtener_columna()
            resultado = disparar(tablero_jugador2, fila, columna)
            print(resultado)
            if resultado == "¡Has golpeado un barco!":
                if jugador_perdio(tablero_jugador2):
                    print("¡El Jugador 1 ha ganado!")
                    break
        else:
            print("Turno del Jugador 2")
            imprimir_tablero(tablero_jugador2)
            fila = obtener_fila()
            columna = obtener_columna()
            resultado = disparar(tablero_jugador1, fila, columna)
            print(resultado)
            if resultado == "¡Has golpeado un barco!":
                if jugador_perdio(tablero_jugador1):
                    print("¡El Jugador 1 ha ganado!")
                    break

        turno = 3 - turno  # Alternar turnos entre jugadores


if __name__ == "__main__":
    juego_de_battleship()
