# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1017

def main(tempo, velocidade):
    quilometrosPorLitro = 12
    distancia = tempo * velocidade

    return '{:.3f}'.format(distancia/quilometrosPorLitro)


assert main(10, 85) == '70.833'
assert main(2, 92) == '15.333'
assert main(22, 67) == '122.833'

tempo = int(input())
velocidade = int(input())

print(main(tempo, velocidade))
