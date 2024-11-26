def area_perimetro():
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro

base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

if __name__ == "__main__":  
    area, perimetro = area_perimetro()  
    print(f"Área: {area}")
    print(f"Perímetro: {perimetro}")
