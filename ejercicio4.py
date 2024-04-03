from collections import Counter

def palindrome_reorder(s):
    # Contamos la frecuencia de cada caracter en la cadena y almacenamos los resultados en el diccionario counts
    counts = Counter(s)
    
    # Creamos una lista llamada odd_count_chars que contiene los caracteres con frecuencia impar en la cadena de entrada
    odd_count_chars = []
    for char, count in counts.items():
        if count % 2 != 0:
            odd_count_chars.append(char)
    
    # Verificamos si hay más de un caracter con una frecuencia impar en la cadena
    if len(odd_count_chars) > 1:
        return "NO SOLUTION"
    
    # Inicializamos una lista llamada palindrome que contendrá los caracteres del palíndromo
    palindrome = []
    
    # Iteramos sobre los elementos del diccionario counts y agregamos la mitad de la frecuencia de cada caracter a la lista palindrome
    for char, count in counts.items():
        palindrome.extend([char] * (count // 2))
    
    # Si hay un caracter con una frecuencia impar en la cadena, lo agregamos al medio del palíndromo
    if odd_count_chars:
        palindrome.append(odd_count_chars[0])
    
    # Para completar el palíndromo, agregamos la parte opuesta del palíndromo sin incluir el caracter impar si existe
    palindrome += palindrome[::-1] if not odd_count_chars else palindrome[::-1][1:]
    
    # Devolvemos la cadena formada por los caracteres del palíndromo
    return ''.join(palindrome)

# Prueba de la función con el caso de prueba proporcionado
assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"

print("Todos los casos de prueba han pasado correctamente.")