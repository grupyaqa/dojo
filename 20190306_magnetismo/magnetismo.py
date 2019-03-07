from math import sqrt


def distancia_entre(p1, p2):
    cateto1 = abs(p1[0] - p2[0])
    cateto2 = abs(p1[1] - p2[1])
    return sqrt(pow(cateto1, 2) + pow(cateto2, 2))
    # return (cateto1**2 + cateto2**2)**0.5


def magnetizar(pontos, raio, cursor):
    pontos_ordenados = sorted([
        ponto
        for ponto in pontos
        if distancia_entre(ponto, cursor) <= raio
    ], key=lambda t: (distancia_entre(t, cursor), t))

    try:
        return next(iter(pontos_ordenados))
    except StopIteration:
        return cursor
