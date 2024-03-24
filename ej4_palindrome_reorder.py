def palindrome_reorder(chain):
    letters_frecuency = {}
    diferences = 0
    palindrome = ""
    aux_letter = ""

#Crear el diccionario con las letras y las veces que se repite
    for letter in chain:
        if letter in letters_frecuency:
            letters_frecuency[letter] += 1
        else:
            letters_frecuency[letter] = 1
            
#Corroborar que sea posible formar un palíndromo
    for value in letters_frecuency.values():
        if value % 2 != 0:
            diferences += 1
            if diferences > 1:
                return print("NO SOLUTION")
            
            
#Construir la mitad del palíndromo y la letra auxiliar que va a ir al medio
    for letter, count in letters_frecuency.items():
        if count % 2 == 0:
            letters_frecuency[letter] = count // 2
        elif count % 2 != 0 and count != 1:
            letters_frecuency[letter] = count -1
            aux_letter = letter


#Construir palindromo completo
    for letter in letters_frecuency.keys():
        palindrome += letter

    if aux_letter:
        palindrome += aux_letter
    
    reversed_palindrome = palindrome[::-1]
    palindrome += reversed_palindrome[1:]
    
    return print(palindrome)


palindrome_reorder("tinaanitalavala")