def number_spiral(x, y):
    if x == y:
        spiral_array = [[],[]]
        for i in range(1,x+1): 
            spiral_array[0].append(i)
            for j in range(1, y+1): 
                spiral_array[1].append(j)
        return print(spiral_array)
    else:
        return print("Los números no son iguales, no se puede hacer un espiral.")

number_spiral(2, 3) 