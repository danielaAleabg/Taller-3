def hallar_mayor_menor(a, b):
    mayor = max(a, b)
    menor = min(a, b)
    return mayor,menor

a = float(input('Ingrese el primer número: '))
b = float(input('Ingrese el segundo número: '))
mayor, menor = hallar_mayor_menor(a, b)
print(f'Mayor: {mayor}, Menor: {menor}')
