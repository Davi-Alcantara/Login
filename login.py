# Importando bibliotecas
import PySimpleGUI as sg
from TestePOO.codigo.base_de_dados import *

# Verificando as planilhas
planilha = selecionar_planilha()
pag_principal = localizar_pagina_principal(planilha)

# Criando janelas
def janela_login():
    sg.theme("Reddit")
    layout = [
        [sg.Text(text='Nome de usuário: '), sg.Input(size=(30, 10), key='usuario')],
        [sg.Text(text='Senha:                '), sg.Input(password_char='*', size=(30, 10), key='senha')],
        [sg.Button(button_text='Logar'), sg.Button(button_text='Criar conta')]

    ]
    return sg.Window('Login', layout=layout, finalize=True)


def nao_existe():
    sg.theme("Reddit")
    layout = [
        [sg.Text(text='Usuário e/ou senha incorretos.')],
        [sg.Button(button_text='Voltar')]

    ]
    return sg.Window('Erro', layout=layout, finalize=True)


def bem_vindo(usuario):
    sg.theme("Reddit")
    layout = [[sg.Text(text=f'Seja bem vindo {usuario}!')],
              [sg.Button(button_text='Voltar')]]
    return sg.Window('Bem vindo', layout=layout, finalize=True)


def criado():
    sg.theme("Reddit")
    layout = [[sg.Text(text='Conta criada com sucesso.')],
              [sg.Button(button_text='Voltar')]
              ]
    return sg.Window('Bem vindo', layout=layout, finalize=True)


janela1, janela2 = janela_login(), None

# Rodando as janelas
while True:
    janela, eventos, valores = sg.read_all_windows()
    if eventos == sg.WIN_CLOSED:
        break
    if janela == janela1 and eventos == 'Logar':
        nome_de_usuario = janela1.Element('usuario').get()
        senha = str(janela1.Element('senha').get())
        verificaco = ler_dados(pagina=pag_principal, nome_de_usuario=nome_de_usuario, senha=senha)
        if verificaco is True:
            janela2 = bem_vindo(nome_de_usuario)
            janela1.hide()
        else:
            janela2 = nao_existe()
            janela1.hide()

    if janela == janela1 and eventos == 'Criar conta':
        nome_de_usuario = janela1.Element('usuario').get()
        senha = str(janela1.Element('senha').get())
        salvar_dados(planilha=planilha, pagina_principal=pag_principal, nome_de_usuario=nome_de_usuario, senha=senha)
        janela2 = criado()
        janela1.hide()
    if janela == janela2 and eventos == 'Voltar':
        janela2.hide()
        janela1 = janela_login()
