#!/usr/bin/python3
'''Programa principal para a conversão de máquinas Mealy e Moore.

Autor: Lucas Possatti
'''

import sexp
import converter
import sys
from optparse import OptionParser

# Define a interface da linha de comando.
usage = "usage: %prog [--input FILE] [--output FILE]"
opt_parse = OptionParser(usage=usage)
opt_parse.add_option("-i", "--input", dest="inputfile_name",
                 help="File to be read which contains the original machine for conversion. `--` for reading from standard input (default).",
                 metavar="FILE", default="--")
opt_parse.add_option("-o", "--output", dest="outputfile_name",
                 help="File where to write the converted machine. `--` for writing to standard output (default).",
                 metavar="FILE", default="--")

# Captura as opções e os argumentos recebidos na linha de comando.
(options, args) = opt_parse.parse_args()

# Verifica os argumentos recebidos.
if len(args) > 0:
	opt_parse.error("This program takes no positional arguments. Only options.")

# Lê a maquina que deve ser convertida.
raw_sexp = ""
if options.inputfile_name == "--":
	# Escreve uma mensagem para o standard error, alertando o usuário que o
	# programa está esperando por ele, se o usuário estiver fornecendo o input
	# por um terminal (e não um pipe, por exemplo).
	if sys.stdin.isatty(): print(">> Waiting for input...", file=sys.stderr)

	# Lê a S-Expression fornecida através do standard input.
	raw_sexp = sys.stdin.read()

	# Se o usuário estiver fornecendo o input através de um terminal, avisa-o
	# de que a sua entrada foi recebida.
	if sys.stdin.isatty(): print(">> Input received.", file=sys.stderr)
else:
	# Lê a S-Expression do arquivo de entrada.
	with open(options.inputfile_name, 'r') as input_file:
		raw_sexp = input_file.read()

# Faz o parsing.
machine = sexp.parse_sexp(raw_sexp)

# Placeholder para a conversão da máquina.
converted_machine = []

# Detecta a máquina e faz a conversão.
if len(machine) == 8 and machine[0] == 'moore':
	converted_machine = converter.moore_to_mealy(machine)
elif len(machine) == 7 and machine[0] == 'mealy':
	converted_machine = converter.mealy_to_moore(machine)
else:
	# Caso a máquina não seja reconhecida, fecha o programa, deixando uma
	# mensagem no standard error.
	print(">> ERROR: The machine could not be recognized neither as a valid "
		"moore machine nor a valid mealy machine. Notice that some members "
		"of the definition may be missing. Possible missing members: "
		"'symbols-in', 'trans' or 'out-fn' (in the case of a moore machine).",
		file=sys.stderr)
	print(">> Exiting with error.", file=sys.stderr)
	exit(1)

# Joga a máquina convertida, de volta para uma S-Expression.
final_sexp = sexp.print_sexp(converted_machine)

# Escreve no arquivo ou imprime a máquina já convertida.
if options.outputfile_name == "--":
	# Imprime o resultado no standard output.
	print(final_sexp)
else:
	# Escreve o resultado em um arquivo.
	with open(options.outputfile_name, 'w') as f:
		f.write(final_sexp + "\n")
