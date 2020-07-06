# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1015

def main(x1, y1, x2, y2):
    distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** (1/2)
    return '{:.4f}'.format(distancia)


assert main(1.0, 7.0, 5.0, 9.0) == '4.4721'
assert main(-2.5, 0.4, 12.1, 7.3) == '16.1484'
assert main(2.5, -0.4, -12.2, 7.0) == '16.4575'

ponto1 = input().split(' ')
ponto2 = input().split(' ')

x1 = float(ponto1[0])
y1 = float(ponto1[1])
x2 = float(ponto2[0])
y2 = float(ponto2[1])

print(main(x1, y1, x2, y2))
