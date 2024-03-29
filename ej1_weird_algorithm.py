def weird_algorithm(n):
    if not isinstance(n, int) or n <1 or n > 10**6:
        return "El numero debe ser un entero positivo"
    array_numbers = []
    
    while n != 1:
        array_numbers.append(n)
        if n % 2 == 0:
            n = n // 2
        else: 
            n = n * 3 + 1
    array_numbers.append(n)

    return array_numbers

assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"

print(weird_algorithm(3))

