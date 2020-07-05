# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1008

numero = int(input())
horas = int(input())
valorPorHora = float(input())

print('NUMBER = {}'.format(numero))
print('SALARY = U$ {:.2f}'.format(horas * valorPorHora))
