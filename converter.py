'''Biblioteca que contém as rotinas de coversão dos diferentes tipos
de máquinas.

Autor: Lucas Possatti
'''

import re

def mealy_to_moore(me):
	'''Converte o parâmetro 'me' (que deve ser uma máquina Mealy) para
	uma máquina de Moore, que é retornada.
	'''
	# Verifica se a máquina recebida, realemente é mealy.
	if me[0] != 'mealy':
		raise 'O método mealy_to_moore esperava receber uma máquina de mealy como entrada.'

	# Cria a máquina de moore.
	moo = ['moore']

#!#	# Procura as trasições com destino a cada um dos estados, para
#!#	# verificar se há mais de uma transição que destina a um único estado.
#!#	for state in me[3][1:]:
#!#		state_trans_outputs = set()
#!#		for trans in me[6][1:]:
#!#			if state == trans[1]:
#!#				pass

	# Inicia um dicionário, com todos os estados como chaves, e um conjunto
	# vazio para seus valores.
	state_outputs = {}
	for state in me[3][1:]:
		state_outputs[state] = set()

	# Busca as saídas que são geradas com a transição para cada um dos estados.
	for trans in me[6][1:]:
		# Verifica se o estado de destino está no dicionário 'state_outputs'.
		if trans[1] not in state_outputs:
			raise "Some transition state destination is not declared in the machine definition (states section). Malformed machine definition."
		state_outputs[trans[1]] = state_outputs[trans[1]].union([trans[3]])

	# Define quais serão os novos estados na máquina de moore.
	moore_states = []
	out_fn = []
	for state in state_outputs:
		# Se o estado tem mais de um output
		if len(state_outputs[state]) > 1:
			# Itera sobre cada um dos outputs desse estado, para gerar os
			# novos estados que forem necessários. Acrescentando '*' para
			# cada novo estado criado.
			i = 0
			for output in state_outputs[state]:
				# Gera o nome para o novo estado.
				new_state = state + '*'*i

				# Adiciona o estado, a lista de estados da nova máquina
				moore_states.append(new_state)

				# Forma a tupla para a função de saída (out-fn).
				out_fn.append([new_state, output])
				i += 1
		# Se o estado tem um único output.
		elif len(state_outputs[state]) == 1:
			# Adiciona o estado, a lista de estados da nova máquina
			moore_states.append(state)

			# Desempacota o conjunto para pegar o seu único elemento que é a
			# saída que o estado deverá gerar.
			(output, ) = state_outputs[state]

			# Forma a tupla para a função de saída (out-fn).
			out_fn.append([state, output])
		# Caso o estado não tenha qualquer output (como por exemplo, se
		# não houver qualquer transição com destino a ele).
		else:
			# Adiciona o estado, a lista de estados da nova máquina
			moore_states.append(state)

			# Forma a tupla para a função de saída (out-fn), no caso
			# o estado não tem qualquer saída.
			out_fn.append([state, []])

	# Gera as transições necessárias para a máquina de moore.
	moore_trans = []
	for trans in me[6][1:]:
		for new_state in moore_states:
			for fn in out_fn:
				#!#print(trans, ":", new_state, ":", fn, "=", re.match("^" + trans[1] + r"\**", new_state) and re.match("^" + trans[1] + r"\**", fn[0]) and trans[3] == fn[1])
				# Usa os vários dados já obtidos para verificar como as
				# transições para a máquina de moore devem ser criadas
				# e quais delas devem ser consideradas.
				if re.match("^" + trans[1] + r"\**", new_state) and re.match("^" + trans[1] + r"\**", fn[0]) and trans[3] == fn[1]:
					# Forma a transição que será adicionada.
					temp_trans = [trans[0], fn[0], trans[2]]

					# Adciona a nova transição, somente se ele já não tiver
					# sido adicionada.
					if temp_trans not in moore_trans:
						moore_trans.append(temp_trans)

	moo.append(["symbols-in"] + me[1][1:])
	moo.append(["symbols-out"] + me[2][1:])
	moo.append(["states"] + moore_states)
	moo.append(["start"] + [me[4][1]])
	moo.append(["finals"] + me[5][1:])
	moo.append(["trans"] + moore_trans)
	moo.append(["out-fn"] + out_fn)

#!#	print('\nDEBUG:')
#!#	print('me[0]', me[0])
#!#	print('me[1]', me[1])
#!#	print('me[2]', me[2])
#!#	print('me[3]', me[3])
#!#	print('me[4]', me[4])
#!#	print('me[5]', me[5])
#!#	print('me[6]', me[6])
#!#	print(':END DEBUG\n')

	return moo

def moore_to_mealy(moo):
	'''Converte o parâmetro 'moo' (que deve ser uma máquina Moore) para
	uma máquina de Mealy, que é retornada.
	'''
	# Verifica se a máquina recebida, realemente é moore.
	if moo[0] != 'moore':
		raise 'O método moore_to_mealy esperava receber uma máquina de moore como entrada.'

	# Cria a máquina de mealy.
	me = ['mealy']

	# Repete os simbolos de entrada e de entrada.
	me.append(['symbols-in'] + moo[1][1:])
	me.append(moo[2])

	# Repete os estados porém adicionando o 'qe'.
	estados = [moo[3][0]] + ['qe'] + moo[3][1:	]
	me.append(estados)

	# O estado inicial é 'qe'.
	me.append(['start', 'qe'])

	# Os estados finais são os mesmos.
	me.append(moo[5])

	# Traduz as transições e saídas da máquina de moore para mealy.
	mealy_trans = []
	moore_trans = moo[6][1:]
	moore_outfn = moo[7][1:]
	for trans in moore_trans:
		# Busca a saída para aquela mudança de estado.
		mealy_trans_output = None
		for out in moore_outfn:
			if out[0] == trans[1]:
				mealy_trans_output = out[1]

		# Forma a transição no formato mealy.
		mealy_trans_stage = [trans[0], trans[1], trans[2], mealy_trans_output]

		# Se a transição for do estado inicial, precisamos adicionalemente
		# acrescenta-la como transição do estado 'qe'
		if mealy_trans_stage[0] == moo[4][1]:
			mealy_trans.append(['qe'] + mealy_trans_stage[1:])

		# E adiciona ao conjunto de transições da máquina mealy.
		mealy_trans.append(mealy_trans_stage)

	# Coloca as transações da mealy dentro da máquina.
	me.append(['trans'] + mealy_trans)

#!#	print('DEBUG:')
#!#	print('moo[0]', moo[0])
#!#	print('moo[1]', moo[1])
#!#	print('moo[2]', moo[2])
#!#	print('moo[3]', moo[3])
#!#	print('moo[4]', moo[4])
#!#	print('moo[5]', moo[5])
#!#	print('moo[6]', moo[6])
#!#	print('moo[7]', moo[7][0:-1])
#!#	print(':END DEBUG')

	return me
