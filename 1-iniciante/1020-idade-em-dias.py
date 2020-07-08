# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1020

def main(dias):
    anos = dias // 365
    dias = dias % 365

    meses = dias // 30
    dias = dias % 30

    return '{} ano(s)\n{} mes(es)\n{} dia(s)'.format(anos, meses, dias)

assert main(400) == '''1 ano(s)
1 mes(es)
5 dia(s)'''

assert main(800) == '''2 ano(s)
2 mes(es)
10 dia(s)'''

assert main(30) == '''0 ano(s)
1 mes(es)
0 dia(s)'''

idadeEmDias = int(input())
print(main(idadeEmDias))
