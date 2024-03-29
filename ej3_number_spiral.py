def number_spiral(F, C):
    # Determinar el orden de la matriz
    if F > C:
        #Calcular el área del cuadrado 
        prev_area = (F - 1) * (F - 1)
        
        # Determinar si las el numero de columnas es par o impar
        if F % 2 != 0:
            #La espiral va en orden creciente
            col_aumento = C
        else:
            #La espiral va en orden decreciente
            col_aumento = 2 * F - C
            
        # Resultado final
        return (prev_area + col_aumento)
    else:
        #Calcular el área del cuadrado 
        prev_area = (C - 1) * (C - 1)

        # Determinar si las el numero de columnas es par o impar
        if C % 2 == 0:
            #La espiral va en orden creciente
            fila_aumento = F
        else:
            #La espiral va en orden decreciente
            fila_aumento = 2 * C - F
            
        # Resultado final
        return (prev_area + fila_aumento)
    
    
assert number_spiral(2, 2) == 3, "Error en el caso de prueba"

print(number_spiral(5,5))