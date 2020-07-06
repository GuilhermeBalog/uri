# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1010

def main(raio):
    volume = float(4/3) * 3.14159 * raio * raio * raio
    return ('VOLUME = {:.3f}'.format(volume))

assert main(3) == 'VOLUME = 113.097'
assert main(15) == 'VOLUME = 14137.155'
assert main(1523) == 'VOLUME = 14797486501.627'

raio = float(input())
print(main(raio))
