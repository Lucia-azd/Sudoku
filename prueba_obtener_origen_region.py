

def obtener_origen_region_3(fila, columna):        
    for i in range(0, 9, 3):
        while i <= fila <= (i+3-1):
            for j in range(0, 9, 3):
                if j <= columna <= (j+3-1):
                    fila = i
                    columna = j
                    posicion = fila, columna 
                    return print(posicion)
                else:
                    continue

def obtener_origen_region_3(fila, columna):        
    for i in range(0, 9, 3):
        while i <= fila <= (i+3-1):
            for j in range(0, 9, 3):
                if j <= columna <= (j+3-1):
                    fila = i
                    columna = j
                    posicion = fila, columna 
                    return posicion

def hay_valor_en_region(fila, columna):
    '''
    Devuelve True si hay hay algún casillero con el valor `valor`
    en la región de 3x3 a la que corresponde la posición (fila, columna).

    Ver como se agrupan las regiones en la documentación de la función
    obtener_origen_region.
    
    Por ejemplo, para la posición (fila = 0, columna = 1) deberán revisar 
    si está `valor` en todas las siguientes celdas:
    (0, 0), (0, 1) (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2).
    '''
    """ for i in range(0,3):
        if obtener_origen_region(fila, columna) """ 

    f, c = obtener_origen_region_3(fila, columna)
    for i in range(0, 3):
        for j in range(0, 3):
            if fila < 10:
                print( f + i, c + j)

    
print('region 1')
obtener_origen_region_3(0,0)
obtener_origen_region_3(0,1)
obtener_origen_region_3(0,2)
obtener_origen_region_3(1,0)
obtener_origen_region_3(1,1)
obtener_origen_region_3(1,2)
obtener_origen_region_3(2,0)
obtener_origen_region_3(2,1)
obtener_origen_region_3(2,2)
print('region 2')
obtener_origen_region_3(0,3)
obtener_origen_region_3(0,4)
obtener_origen_region_3(0,5)
obtener_origen_region_3(1,3)
obtener_origen_region_3(1,4)
obtener_origen_region_3(1,5)
obtener_origen_region_3(2,3)
obtener_origen_region_3(2,4)
obtener_origen_region_3(2,5)
print('region 3')
obtener_origen_region_3(0,6)
obtener_origen_region_3(0,7)
obtener_origen_region_3(0,8)
obtener_origen_region_3(1,6)
obtener_origen_region_3(1,7)
obtener_origen_region_3(1,8)
obtener_origen_region_3(2,6)
obtener_origen_region_3(2,7)
obtener_origen_region_3(2,8)

print('region 4')
obtener_origen_region_3(3,0)
obtener_origen_region_3(3,1)
obtener_origen_region_3(3,2)
obtener_origen_region_3(4,0)
obtener_origen_region_3(4,1)
obtener_origen_region_3(4,2)
obtener_origen_region_3(5,0)
obtener_origen_region_3(5,1)
obtener_origen_region_3(5,2)
print('region 5')
obtener_origen_region_3(3,3)
obtener_origen_region_3(3,4)
obtener_origen_region_3(3,5)
obtener_origen_region_3(4,3)
obtener_origen_region_3(4,4)
obtener_origen_region_3(4,5)
obtener_origen_region_3(5,3)
obtener_origen_region_3(5,4)
obtener_origen_region_3(5,5)
print('region 6')
obtener_origen_region_3(3,6)
obtener_origen_region_3(3,7)
obtener_origen_region_3(3,8)
obtener_origen_region_3(4,6)
obtener_origen_region_3(4,7)
obtener_origen_region_3(4,8)
obtener_origen_region_3(5,6)
obtener_origen_region_3(5,7)
obtener_origen_region_3(5,8)

print('region 7')
obtener_origen_region_3(6,0)
obtener_origen_region_3(6,1)
obtener_origen_region_3(6,2)
obtener_origen_region_3(7,0)
obtener_origen_region_3(7,1)
obtener_origen_region_3(7,2)
obtener_origen_region_3(8,0)
obtener_origen_region_3(8,1)
obtener_origen_region_3(8,2)
print('region 8')
obtener_origen_region_3(6,3)
obtener_origen_region_3(6,4)
obtener_origen_region_3(6,5)
obtener_origen_region_3(7,3)
obtener_origen_region_3(7,4)
obtener_origen_region_3(7,5)
obtener_origen_region_3(8,3)
obtener_origen_region_3(8,4)
obtener_origen_region_3(8,5)
print('region 9')
obtener_origen_region_3(6,6)
obtener_origen_region_3(6,7)
obtener_origen_region_3(6,8)
obtener_origen_region_3(7,6)
obtener_origen_region_3(7,7)
obtener_origen_region_3(7,8)
obtener_origen_region_3(8,6)
obtener_origen_region_3(8,7)
obtener_origen_region_3(8,8)


""" obtener_origen_region(1,2)
obtener_origen_region(1,3)
obtener_origen_region(2,2)
obtener_origen_region(2,3)
obtener_origen_region(2,1)
obtener_origen_region(3,1)
obtener_origen_region(3,2)
obtener_origen_region(3,3) """