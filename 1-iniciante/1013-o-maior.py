# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1013

def main(input):
    dados = input.split(' ')

    a = int(dados[0])
    b = int(dados[1])
    c = int(dados[2])

    maior = maiorAB(a, b)
    maior = maiorAB(maior, c)

    return '{} eh o maior'.format(maior)

def maiorAB(a, b):
    # Formula tirado do enunciado
    return int((a + b + abs(a - b))/2)

assert main('7 14 106') == '106 eh o maior', 'Deveria ser 106'
assert main('217 14 6') == '217 eh o maior', 'Deveria ser 217'
assert main('2 14 6') == '14 eh o maior', 'Deveria ser 14'
assert main('2 2 2') == '2 eh o maior', 'Deveria ser 2'

entrada = input()
print(main(entrada))
