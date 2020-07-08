# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1038

precos = [4, 4.5, 5, 2, 1.5]

entrada = input().split(' ')
produto = int(entrada[0]) - 1
quantidade = int(entrada[1])

print('Total: R$ {:.2f}'.format(quantidade * precos[produto]))
