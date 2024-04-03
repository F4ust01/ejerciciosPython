def weird_algorithm(n):
    ans = [n]  
    while n != 1:
        if n % 2 == 0:
            n = n // 2 
        else:
            n = (n * 3) + 1  
        ans.append(n)
    return ans

assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"

print("Todos los casos de prueba han pasado correctamente.")