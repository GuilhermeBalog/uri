# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1019

def main(segundos):
    horas = segundos // 3600
    segundos = segundos % 3600
    
    minutos  = segundos // 60
    segundos = segundos % 60

    return '{}:{}:{}'.format(horas, minutos, segundos)

segundos = int(input())
print(main(segundos))

assert main(140153) == '38:55:53'
assert main(1) == '0:0:1'
assert main(556) == '0:9:16'