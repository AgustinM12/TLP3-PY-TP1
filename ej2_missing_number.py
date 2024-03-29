def missing_number(limit, array): 
    if len(array) == limit - 1:

        for position in array:  
            if not isinstance(position, int):
                return "Los elementos del array deben ser enteros"
        for number in range(1, limit):
            if number not in array:
                return number
assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"

print(missing_number(5, [1, 2, 4, 5])) 