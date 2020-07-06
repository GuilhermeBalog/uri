# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1018

def main(montante):
    cedulas = [100, 50, 20, 10, 5, 2, 1]

    resultado = '{}'.format(montante)
    for cedula in cedulas:
        resultado += '\n{} nota(s) de R$ {},00'.format(int(montante/cedula), cedula)
        montante %= cedula

    return resultado

assert main(576) == '576\n5 nota(s) de R$ 100,00\n1 nota(s) de R$ 50,00\n1 nota(s) de R$ 20,00\n0 nota(s) de R$ 10,00\n1 nota(s) de R$ 5,00\n0 nota(s) de R$ 2,00\n1 nota(s) de R$ 1,00'
assert main(11257) == '11257\n112 nota(s) de R$ 100,00\n1 nota(s) de R$ 50,00\n0 nota(s) de R$ 20,00\n0 nota(s) de R$ 10,00\n1 nota(s) de R$ 5,00\n1 nota(s) de R$ 2,00\n0 nota(s) de R$ 1,00'
assert main(503) == '503\n5 nota(s) de R$ 100,00\n0 nota(s) de R$ 50,00\n0 nota(s) de R$ 20,00\n0 nota(s) de R$ 10,00\n0 nota(s) de R$ 5,00\n1 nota(s) de R$ 2,00\n1 nota(s) de R$ 1,00'

montante = int(input())
print(main(montante))