# Función que separa la lista en pares e impares
def Separar(lista):
    pares = []
    impares = []
    
    # Recorremos la lista original y separamos los números pares e impares
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    
    # Ordenamos las listas
    pares.sort()
    impares.sort()
    
    # Modificamos la lista original para reflejar los números ordenados
    lista.clear()  # Limpiar la lista original
    lista.extend(pares)  # Añadir los pares primero
    lista.extend(impares)  # Añadir los impares después
    
    # Imprimimos los resultados
    print("Lista modificada:", lista)

# Lista de números
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Llamada a la función para separar la lista en pares e impares
Separar(numeros)

# Lista modificada
print("Lista después de la modificación:", numeros)

