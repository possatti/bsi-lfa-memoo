'''Biblioteca que contém as rotinas de coversão dos diferentes tipos
de máquinas.

Autor: Lucas Possatti
'''

def mealy_to_moore(me):
	'''Converte o parâmetro 'me' (que deve ser uma máquina Mealy) para
	uma máquina de Moore, que é retornada.
	'''
	pass

def moore_to_mealy(moo):
	'''Converte o parâmetro 'moo' (que deve ser uma máquina Moore) para
	uma máquina de Mealy, que é retornada.
	'''
	# Verifica se a máquina recebida, realemente é moore.
	if moo[0] != 'moore':
		raise 'O método moore_to_mealy espera receber uma máquina de moore como entrada.'

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
		#print('trans:' + str(trans))
		for out in moore_outfn:
			#print(out[0] + '==' + trans[1] + ':' + str(out[0] == trans[1]))
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

	print('DEBUG:')
	print('moo[0]', moo[0])
	print('moo[1]', moo[1])
	print('moo[2]', moo[2])
	print('moo[3]', moo[3])
	print('moo[4]', moo[4])
	print('moo[5]', moo[5])
	print('moo[6]', moo[6])
	print('moo[7]', moo[7][0:-1])
	print(':END DEBUG')

	return me
