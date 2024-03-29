def palindrome_reorder(chain):
    if chain.isalpha() and chain.islower() and 1 <= len(chain) <= 10**6 and "ñ" not in chain:
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
                    return "NO SOLUTION"
                
    #Construir la mitad del palíndromo y la letra auxiliar que va a ir al medio
        for letter, count in letters_frecuency.items():
            if count % 2 == 0:
                letters_frecuency[letter] = count // 2
            elif count % 2 != 0 and count != 1:
                letters_frecuency[letter] = count -1
                letters_frecuency[letter] = count // 2
                aux_letter = letter

    #Construir palindromo completo
        for letter, count in letters_frecuency.items():
            while count > 0:
                palindrome += letter
                count -= 1

        if aux_letter:
            palindrome += aux_letter
        
        reversed_palindrome = palindrome[::-1]
        palindrome += reversed_palindrome[1:]
        
        return palindrome
    else: 
        return "La cadena no cumple con las condiciones" 

assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"

print(palindrome_reorder("ayarrbybyyowoyw"))