def suma():
    return num1 + num2

def resta():
    return num1 - num2

def multiplicacion():
    return num1 * num2

def division():
    if num2 != 0:
        return num1 / num2
    else:
        return 'Error: División por cero'

def potencia():
    return num1 ** num2

def porcentaje():
    return (num1 * num2) / 100

def raiz():
    if num1 >= 0:
        return math.sqrt(num1)
    else:
        return 'Error: No se puede calcular la raíz de un número negativo'

while True:
    print('''Menú de operaciones:
          1. Suma.
          2. Resta.
          3. Multiplicación.
          4. División.
          5. Potencia.
          6. Porcentaje.
          7. Raíz cuadrada.
          8. Salir.''')
    opcion = int(input('Seleccione una opción: '))

    if opcion == 8:
        break

    num1 = float(input('Ingrese el primer número: '))
    num2 = float(input('Ingrese el segundo número: '))

    if opcion == 1:
        print(f'Resultado: {suma()}')
    elif opcion == 2:
        print(f'Resultado: {resta()}')
    elif opcion == 3:
        print(f'Resultado: {multiplicacion()}')
    elif opcion == 4:
        print(f'Resultado: {division()}')
    elif opcion == 5:
        print(f'Resultado: {potencia()}')
    elif opcion == 6:
        print(f'Resultado: {porcentaje()}')
    elif opcion == 7:
        print(f'Resultado: {raiz()}')
    else:
        print('Opción no válida')
