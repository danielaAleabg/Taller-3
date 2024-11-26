def relacion():
    if num1 > num2:
        return 'True'
    elif num1 < num2:
        return 'False'
    else:
        return 'Empate'

num1 = float(input('Ingrese el primer número: '))
num2 = float(input('Ingrese el segundo número: '))
print(relacion())
