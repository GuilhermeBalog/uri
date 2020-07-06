# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1012

def main(a, b, c):
    resultado = ''

    resultado += 'TRIANGULO: {:.3f}'.format(triangulo(a, c))
    resultado += '\nCIRCULO: {:.3f}'.format(circulo(c))
    resultado += '\nTRAPEZIO: {:.3f}'.format(trapezio(a, b, c))
    resultado += '\nQUADRADO: {:.3f}'.format(quadrado(b))
    resultado += '\nRETANGULO: {:.3f}'.format(retangulo(a, b))

    return resultado

def triangulo(base, altura):
    return (base * altura)/2

def circulo(raio):
    return 3.14159 * raio * raio

def trapezio(base1, base2, altura):
    return (base1 + base2) * altura / 2

def quadrado(lado):
    return lado * lado

def retangulo(base, altura):
    return base * altura

assert main(3.0, 4.0, 5.2) == 'TRIANGULO: 7.800\nCIRCULO: 84.949\nTRAPEZIO: 18.200\nQUADRADO: 16.000\nRETANGULO: 12.000'
assert main(12.7, 10.4, 15.2) == 'TRIANGULO: 96.520\nCIRCULO: 725.833\nTRAPEZIO: 175.560\nQUADRADO: 108.160\nRETANGULO: 132.080'

dados = input().split(' ')

a = float(dados[0])
b = float(dados[1])
c = float(dados[2])

print(main(a, b, c))