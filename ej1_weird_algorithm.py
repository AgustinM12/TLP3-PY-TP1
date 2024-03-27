def weird_algorithm(n):
    if n < 1 or type(n) != int or n > 10**6:
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

print(weird_algorithm(3))

