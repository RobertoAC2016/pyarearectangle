# Calculo del area de un rectangula con python
# @raccoding
#

# if __name__ == '__main__':
#     base = float(input('Introduce la base del rectangulo: '))
#     altura = float(input('Introduce la altura del rectangulo: '))
#     area = calcular_area_rectangulo(base, altura)
#     print(f'El area del rectangulo es: {area}')


# base = float(input('Introduce la base del rectangulo: '))
# altura = float(input('Introduce la altura del rectangulo: '))
# area = calcular_area_rectangulo(base, altura)
# print(f'El area del rectangulo es: {area}')

def calcular_area_rectangulo(base, altura):
    return base * altura

def main():
    base = float(input('Introduce la base del rectangulo: '))
    altura = float(input('Introduce la altura del rectangulo: '))
    area = int(calcular_area_rectangulo(base, altura))
    print(f'El area del rectangulo es: {area}')

if __name__ == '__main__':
    main()
