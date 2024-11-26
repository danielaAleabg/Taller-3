import math

def area_perimetro_circulo(radio):
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
    return area, perimetro

radio = float(input('Ingrese el radio del círculo: '))
area, perimetro = area_perimetro_circulo(radio)
print(f'Área: {area}, Perímetro: {perimetro}')
