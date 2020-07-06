# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1016

def main(distancia):
    return '{} minutos'.format(distancia*2)


assert main(30) == '60 minutos'
assert main(110) == '220 minutos'
assert main(7) == '14 minutos'

distancia = int(input())

print(main(distancia))
