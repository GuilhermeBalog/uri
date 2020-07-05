# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1009

nome = input()
salario = float(input())
valorDasVendas = float(input())

print('TOTAL = R$ {:.2f}'.format(salario + (valorDasVendas * 0.15)))
