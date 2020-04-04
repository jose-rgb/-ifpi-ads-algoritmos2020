def main():
    x1 = int(input('Qual á coordenada X do primeiro ponto: '))
    y1 = int(input('Qual á coordenada Y do primeiro ponto: '))
    x2 = int(input('Qual á coordenada X do segundo ponto: '))
    y2 = int(input('Qual á coordenada Y do segundo ponto: '))
    x = calculo_x(x1, x2)
    y = calculo_y(y1, y2)
    area = calculo_area(x, y)
    print(f'A área do retângulo formado por essas coordenadas no plano cartesiano é {area} m²')


def calculo_x(x1, x2):
    if x1 > x2:
        x = x1 - x2
        return x
    elif x1 < x2:
        x = x2 - x1
        return x
    else:
        return x1


def calculo_y(y1, y2):
    if y1 > y2:
        y = y1 - y2
        return y
    elif y1 < y2:
        x = y2 - y1
        return x
    else:
        return y1


def calculo_area(x, y):
    area = x * y
    return area


main()
