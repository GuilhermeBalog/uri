# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1014

def main(distancia, combustivelGasto):
    return '{:.3f} km/l'.format(distancia/combustivelGasto)


assert main(500, 35.0) == '14.286 km/l'
assert main(2254, 124.4) == '18.119 km/l'
assert main(4554, 464.6) == '9.802 km/l'

distancia = int(input())
combustivelGasto = float(input())

print(main(distancia, combustivelGasto))
