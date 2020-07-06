# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1010

peca1 = input().split(' ')
peca2 = input().split(' ')

codigo = 0
quantidade = 1
valorUnitario = 2

total = int(peca1[quantidade]) * float(peca1[valorUnitario]) + int(peca2[quantidade]) * float(peca2[valorUnitario])

print('VALOR A PAGAR: R$ {:.2f}'.format(total))
