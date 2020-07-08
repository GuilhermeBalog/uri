# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1036

linha = input().split(' ')
a = float(linha[0])
b = float(linha[1])
c = float(linha[2])

delta = (b**2) - (4 * a * c)

if delta < 0 or a == 0:
    print('Impossivel calcular')
else:
    print('R1 = {:.5f}'.format((-b + (delta** (1/2))) / (2*a)))
    print('R2 = {:.5f}'.format((-b - (delta** (1/2))) / (2*a)))

