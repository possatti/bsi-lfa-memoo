#!/usr/bin/python3
'''Programa principal para a conversão de máquinas Mealy e Moore.

Autor: Lucas Possatti
'''

import sexp
import converter
import sys

# Lê a S-Expression fornecida através do stdin.
sexp = sys.stdin.read()

# Imprime a máquina lida.
print('>> Original machine:\n%s\n' % sexp)

# Faz o parsing.
machine = sexpr.parse_sexp(sexp)

# Placeholder para a conversão da máquina.
converted_machine = []

# Detecta a máquina e faz a conversão.
if machine[0] == 'moore':
	converted_machine = converter.moore_to_mealy(machine)
elif machine[0] == 'mealy':
	converted_machine = converter.moore_to_mealy(machine)
else:
	raise "A máquina indicada não pode ser reconhecida."


# Joga a máquina convertida, de volta para uma S-Expression.
final_sexp = sexpr.print_sexp(converted_machine)

# Imprime a máquina já convertida.
print(">> Converted machine:\n%s\n" % final_sexp)
