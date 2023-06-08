from string import ascii_uppercase
from tkinter.messagebox import showerror

tabela_referencia = list(ascii_uppercase)


class Commands:
	def __init__(self, master):
		self.master = master

	def Grade(self):
		grade = list()
		for alfabeto in range(0, 26):
			if alfabeto == 0:
				grade.append(tabela_referencia)
			else:
				grade.append(tabela_referencia[alfabeto:])
				grade[alfabeto].extend(tabela_referencia[:alfabeto])

		return grade

	def traduzir(self):
		if not self.master.chave.get() or not self.master.mensagem.get():
			showerror('Erro', 'Preenche corretamente')
			return
		if self.master.descriptografar.get():
			self.descriptografar(self.master.mensagem.get(), self.master.chave.get(), self.master.grade)
		else:
			self.criptografar(self.master.mensagem.get(), self.master.chave.get(), self.master.grade)

	def criptografar(self, msg, chave, grade):
		msg = msg.strip().upper().split()
		msg = ' '.join(msg)
		chave = chave.replace(' ', '').upper()

		msg_final = list()
		c = 0
		for letra in msg:
			if letra in tabela_referencia:
				if c == len(chave):
					c = 0
				posicao_letra_msg_alfabeto = tabela_referencia.index(letra)
				posicao_letra_chave_alfabeto = tabela_referencia.index(chave[c])
				msg_final.append(grade[posicao_letra_chave_alfabeto][posicao_letra_msg_alfabeto])
				c += 1
			else:
				msg_final.append(letra)
				continue

		msg_final = ''.join(msg_final)
		self.master.mensagem_final.set(value=msg_final)


	def descriptografar(self, msg, chave, grade):
		msg = msg.strip().upper().split()
		msg = ' '.join(msg)
		chave = chave.replace(' ', '').upper()

		msg_final = list()
		c = 0
		for letra in msg:
			if letra in tabela_referencia:
				if c == len(chave):
					c = 0
				posicao_letra_chave_alfabeto = tabela_referencia.index(chave[c])
				posicao_letra_msg_alfabeto = grade[posicao_letra_chave_alfabeto].index(letra)
				msg_final.append(tabela_referencia[posicao_letra_msg_alfabeto])
				c += 1
			else:
				msg_final.append(letra)
				continue
		msg_final = ''.join(msg_final)
		self.master.mensagem_final.set(value=msg_final)
