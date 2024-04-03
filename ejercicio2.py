def missing_number(length, n):
    ans = 0
    for i in range(len(n)-1):  # Iterar hasta el penúltimo elemento
        if n[i] != n[i+1] - 1:
            ans = n[i] + 1
            break
    if ans == 0:  # Si ningún número falta, devolver el último número más 1
        ans = n[-1] + 1
    return ans

assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"

print("Todos los casos de prueba han pasado correctamente.")