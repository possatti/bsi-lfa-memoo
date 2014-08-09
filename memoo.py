#!/usr/bin/python3
'''Programa principal para a conversão de máquinas Mealy e Moore.

Autor: Lucas Possatti
'''

import sexp
import converter
from sys import stdin
from optparse import OptionParser

# Define a interface da linha de comando.
opt_parse = OptionParser()
opt_parse.add_option("-i", "--input", dest="inputfile_name",
                 help="File to be read which contains the original machine for conversion. `--` for reading from standard input (default).",
                 metavar="FILE", default="--")
opt_parse.add_option("-o", "--output", dest="outputfile_name",
                 help="File where to write the converted machine. `--` for writing to standard output (default).",
                 metavar="FILE", default="--")

# Captura as opções e os argumentos recebidos na linha de comando.
(options, args) = opt_parse.parse_args()

# Lê a maquina que deve ser convertida.
raw_sexp = ""
if options.inputfile_name == "--":
	# Lê a S-Expression fornecida através do standard input.
	raw_sexp = stdin.read()
else:
	# Lê a S-Expression do arquivo de entrada.
	with open(options.inputfile_name, 'r') as input_file:
		raw_sexp = input_file.read()

# Imprime a máquina lida (DEBUG).
print('>> Original machine:\n%s\n' % raw_sexp)

# Faz o parsing.
machine = sexp.parse_sexp(raw_sexp)

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
final_sexp = sexp.print_sexp(converted_machine) + "\n"

# Escreve no arquivo ou imprime a máquina já convertida.
if options.outputfile_name == "--":
	# Imprime o resultado no standard output.
	print(final_sexp)
	#writer.print_machine(converted_machine)
else:
	# Escreve o resultado em um arquivo.
	with open(options.outputfile_name, 'w') as f:
		f.write(final_sexp)
	#writer.write_machine_to_file(converted_machine, options.outputfile_name)
