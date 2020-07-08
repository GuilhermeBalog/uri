# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1021

def main(quantia):
    reais = int(quantia.split('.')[0])
    centavos = int(quantia.split('.')[1])

    resultado = ''

    notas = [100, 50, 20, 10, 5, 2]
    moedas = [50, 25, 10, 5, 1]

    resultado += 'NOTAS:'
    for nota in notas:
        quantidade = reais // nota
        reais = reais % nota

        resultado += '\n{} nota(s) de R$ {:.2f}'.format(quantidade, nota)

    resultado += '\nMOEDAS:'
    resultado += '\n{} moeda(s) de R$ {:.2f}'.format(reais, 1)
    for moeda in moedas:
        quantidade = centavos // moeda
        centavos = centavos % moeda

        resultado += '\n{} moeda(s) de R$ 0.{:0>2}'.format(quantidade, moeda)

    return resultado

quantia = input()
print(main(quantia))

assert main('576.73') == '''NOTAS:
5 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
2 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
3 moeda(s) de R$ 0.01'''

assert main('4.00') == '''NOTAS:
0 nota(s) de R$ 100.00
0 nota(s) de R$ 50.00
0 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
0 nota(s) de R$ 5.00
2 nota(s) de R$ 2.00
MOEDAS:
0 moeda(s) de R$ 1.00
0 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
0 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
0 moeda(s) de R$ 0.01'''

assert main('91.01') == '''NOTAS:
0 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
2 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
0 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
0 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
0 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
1 moeda(s) de R$ 0.01'''

assert main('0.02') == '''NOTAS:
0 nota(s) de R$ 100.00
0 nota(s) de R$ 50.00
0 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
0 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
0 moeda(s) de R$ 1.00
0 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
0 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
2 moeda(s) de R$ 0.01'''

assert main('0.35') == '''NOTAS:
0 nota(s) de R$ 100.00
0 nota(s) de R$ 50.00
0 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
0 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
0 moeda(s) de R$ 1.00
0 moeda(s) de R$ 0.50
1 moeda(s) de R$ 0.25
1 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
0 moeda(s) de R$ 0.01'''

assert main('849.00') == '''NOTAS:
8 nota(s) de R$ 100.00
0 nota(s) de R$ 50.00
2 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
2 nota(s) de R$ 2.00
MOEDAS:
0 moeda(s) de R$ 1.00
0 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
0 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
0 moeda(s) de R$ 0.01'''

assert main('312.88') == '''NOTAS:
3 nota(s) de R$ 100.00
0 nota(s) de R$ 50.00
0 nota(s) de R$ 20.00
1 nota(s) de R$ 10.00
0 nota(s) de R$ 5.00
1 nota(s) de R$ 2.00
MOEDAS:
0 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
1 moeda(s) de R$ 0.25
1 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
3 moeda(s) de R$ 0.01'''