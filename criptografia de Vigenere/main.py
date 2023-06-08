from tkinter import *
from tkinter import ttk
from commands import *
from pyperclip import copy

class Vigenere(Tk):
    def __init__(self):
        super().__init__()

        self.commands = Commands(self)

        self.grade = self.commands.Grade()
        self.configurar_janela()


    def configurar_janela(self):
        self.frame_inputs = ttk.LabelFrame(self)
        self.frame_botoes = ttk.LabelFrame(self)

        self.mensagem_final = StringVar()
        ttk.Label(self.frame_botoes, textvariable=self.mensagem_final).pack(side='top')

        self.configurar_inputs_botoes()

        self.frame_inputs.pack(side='top', expand=True, fill='x')
        self.frame_botoes.pack(side='bottom', expand=True, fill='x')

    def configurar_inputs_botoes(self):
        ttk.Label(self.frame_inputs, text='Mensagem sem acentuação').pack(side='top')
        self.mensagem = StringVar()
        entry_mensagem = ttk.Entry(self.frame_inputs, textvariable=self.mensagem)
        entry_mensagem.pack(side='top')

        ttk.Label(self.frame_inputs, text='Chave sem acentuação').pack(side='top')
        self.chave = StringVar()
        entry_chave = ttk.Entry(self.frame_inputs, textvariable=self.chave)
        entry_chave.pack(side='top')

        self.descriptografar = BooleanVar()
        checkbox_descriptografar = ttk.Checkbutton(self.frame_inputs, variable=self.descriptografar)
        checkbox_descriptografar.pack(side='bottom')
        ttk.Label(self.frame_inputs, text='Descriptografar').pack(side='bottom')

        botao_traduzir = ttk.Button(self.frame_botoes, text='Traduzir', command=self.commands.traduzir)
        botao_copiar = ttk.Button(self.frame_botoes, text='Copiar', command=lambda : copy(self.mensagem_final.get()))

        botao_traduzir.pack(side='right')
        botao_copiar.pack(side='left')

if __name__ == '__main__':
    app = Vigenere()
    app.title('Vigenere')
    app.geometry('200x200')
    app.mainloop()
