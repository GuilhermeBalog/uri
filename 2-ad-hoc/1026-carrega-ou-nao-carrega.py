# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1026

while True:
    try:
        linha = input().split(' ')
        a = int(linha[0])
        b = int(linha[1])

        print(a.__xor__(b))
    except EOFError:
        break