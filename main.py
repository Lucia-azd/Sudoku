import sudoku as sudoku_importado
import random
import mapas

def imprimir_sudoku(sudoku, indice_fila):
    """ Recibe un sudoku y lo imprime """

    inicio = 0
    fin = 3
    print('\n\n     1 ', '2 ', '3 ','   4 ', '5 ', '6 ','   7 ', '8 ', '9')
    print('  ╔══════════════════════════════════╗\n', end='')
    
    sudoku_a_imprimir = []
    for f in range(len(sudoku)):
        sudoku_a_imprimir.append([])
        for c in range(len(sudoku[f])):
            if sudoku_importado.obtener_valor(sudoku, f, c) == sudoku_importado.VACIO:
                sudoku_a_imprimir[f].append('·')
            else:
                sudoku_a_imprimir[f].append(sudoku[f][c])
    
    while inicio <= 6 and fin <= 9:
        for f in range(inicio, fin):
            print(indice_fila[f] ,'║', end= '')
            for c in range(0, 9):
                if c == 2:
                    print(' ', sudoku_a_imprimir[f][c], ' |', end='')
                elif c == 5:
                    print(' ', sudoku_a_imprimir[f][c], ' |', end='')
                else:
                    print(' ', sudoku_a_imprimir[f][c], end='')
            print(' ║', indice_fila[f])
            
            if f == 2 or f == 5 :
                print('  ╠══════════════════════════════════╣') 
        inicio = inicio + 3
        fin = fin + 3
    
    print('  ╚══════════════════════════════════╝\n', end='')
    print('     1 ', '2 ', '3 ','   4 ', '5 ', '6 ','   7 ', '8 ', '9\n')

def cambiar_valor(movimiento ,indice_fila, indice_columna):
    """ Cambia el valor de los elementos de movimiento por el indice de su posicion """

    for item_f in indice_fila:
        if movimiento[0] == item_f:
            movimiento[0] = indice_fila.index(item_f)
        
    for item_c in indice_columna:
        if movimiento[1] == item_c:
            movimiento[1] = indice_columna.index(item_c)
    return movimiento

def verificar_movimiento(mensaje_error, movimiento, indice_fila, indice_columna):
    """ Verifica que los movimiento de movimiento pasado por parametro se encuentren dentro de los inidices de las filas y las columnas """

    if len(movimiento) <= 2:
        while not(movimiento[0] in indice_fila) or not(movimiento[1] in indice_columna):
            valor_correcto = input(mensaje_error)
            movimiento = valor_correcto.split(", ")

        movimiento = cambiar_valor(movimiento, indice_fila, indice_columna)
        return movimiento
    else:
        while not(movimiento[0] in indice_fila) or not(movimiento[1] in indice_columna) or not(movimiento[2] in indice_columna):
            movimiento_correcto = input(mensaje_error)
            movimiento = movimiento_correcto.split(", ")
        
        movimiento = cambiar_valor(movimiento, indice_fila, indice_columna)
        return movimiento

def iniciar_juego():

    sudoku_aleatorio = random.choice(mapas.MAPAS)
    sudoku_mapa = sudoku_importado.crear_juego(sudoku_aleatorio)

    indice_fila = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    indice_columna = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    imprimir_sudoku(sudoku_mapa, indice_fila)
    
    while not(sudoku_importado.esta_terminado(sudoku_mapa)):
        movimiento_jugador = input('» Ingrese su proximo movimiento [fila, columna, valor] \n\n» "borrar" para borrar un valor\n\n» "salir" para abandonar el juego: ')
        
        if movimiento_jugador == "borrar":
            valor_a_borrar = input('Posición del valor a borrar [fila, columna]: ')
            posicion = valor_a_borrar.split(", ")
            
            posicion = verificar_movimiento('¡Error! Por favor elija una posición valida entre las que figuran en pantalla: ', posicion, indice_fila, indice_columna)

            sudoku_mapa = sudoku_importado.borrar_valor(sudoku_mapa, posicion[0], posicion[1])
            imprimir_sudoku(sudoku_mapa, indice_fila)

        elif movimiento_jugador == "salir":
            print('\n\nGracias por jugar al SUDOKU ¡Adios!\n\n')
            return 

        else: 
            movimiento = movimiento_jugador.split(", ")

            movimiento = verificar_movimiento('¡Error! Por favor elija un valor entre 1 - 9 y una posición valida entre las que figuran en pantalla: ', movimiento, indice_fila, indice_columna)
            
            while not(sudoku_importado.es_movimiento_valido(sudoku_mapa, movimiento[0], movimiento[1], int(movimiento[2]))):
                movimiento_valido = input(' Movimiento invalido - Ingrese su proximo movimiento [fila, columna, valor]: ')
                movimiento = movimiento_valido.split(", ")
                
                movimiento = verificar_movimiento('¡Error! Por favor elija un valor entre 1 - 9 y una posición valida entre las que figuran en pantalla: ', movimiento, indice_fila, indice_columna)
            
            sudoku_mapa = sudoku_importado.insertar_valor(sudoku_mapa, movimiento[0], movimiento[1], int(movimiento[2]))
            imprimir_sudoku(sudoku_mapa, indice_fila)
        
    print('\n\n¡FELICITACIONES! Ganaste el SUDOKU!\n\n')

iniciar_juego()