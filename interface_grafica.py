# outro comando: import PySimpleGUI as sg

from PySimpleGUI import PySimpleGUI as sg

# Instalar o PySimpleGUI

def tela_ini():
    """
     Cria ou abre a janela inicial do programa com suas configurações.
    Return: Sem retorno.
    """
    sg.theme('Reddit')

    coluna1 = [
        [sg.Text('LOGRADOURO', font='arial 12', pad=(5, 2))],
        [sg.Text('BAIRRO', font='arial 12', pad=(5, 2))],
        [sg.Text('LOCALIDADE', font='arial 12', pad=(5, 2))],
        [sg.Text('UNIDADE FEDERATIVA', font='arial 12', pad=(5, 2))],
        [sg.Text('DDD', font='arial 12', pad=(5, 2))]
    ]

    coluna2 = [
        [sg.Text('ESTADO', font='arial 12', pad=(5, 2))],
        [sg.Text('CIDADES RELACIONADAS', font='arial 12', pad=(5, 2))]
    ]

    layout = [
        [sg.Text('Consulte o CEP ou DDD do Brasil', font='arial 20 bold')],
        [sg.Text('Seja bem vindo!', font='arial 14', pad=(0, 0))],
        [sg.Text('Faça consulta de CEP e DDD para estados e cidades do Brasil', font='arial 14', pad=(0, 0))],
        [sg.Button('CEP', font='arial 12', size=(8, 1), pad=(88, (30, 10))),
         sg.Button('DDD', font='arial 12', size=(8, 1), pad=(100, (30, 10)))],
        [sg.Frame(layout=coluna1, title='', element_justification='center', pad=(30, 0)),
         sg.Frame(layout=coluna2, title='', element_justification='center', pad=(30, (0, 104)))],
        [sg.CButton('Sair', font='arial 12', size=(8, 1), pad=(0, (50, 0)))],
        [sg.Text('Julio©', pad=(0, (35, 0)))]


    ]
    telaprin = sg.Window('Consulta Brasil', element_justification='center', element_padding=(0, 10),
                         layout=layout, size=(800, 500), finalize=True)


def tela_cep():
    """
     Cria ou abre a janela de consulta CEP e suas configurações.
    Return: Sem retorno
    """
    sg.theme('Reddit')

    cep = [
        [sg.Text('Digite o CEP (digite 8 números seguidos sem o traço "-")', font='arial 12', pad=(0, 0))],
        [sg.Input(size=(20, 0), font='arial 12', pad=(0, 0), key='cep', background_color='white')],
        [sg.Button('Consultar', font='arial 12', size=(10, 1))]
    ]

    coluna1 = [
        [sg.Text('LOGRADOURO:', font='arial 12')],
        [sg.Text('BAIRRO:', font='arial 12')],
        [sg.Text('LOCALIDADE:', font='arial 12')],
        [sg.Text('UF:', font='arial 12')],
        [sg.Text('DDD:', font='arial 12')]
    ]

    coluna2 = [
        [sg.Input(font='arial 12 bold', background_color='white', key='logradouro', size=(35, 1))],
        [sg.Input(font='arial 12 bold', background_color='white', key='bairro', size=(30, 1))],
        [sg.Input(font='arial 12 bold', background_color='white', key='localidade', size=(30, 1))],
        [sg.Input(font='arial 12 bold', background_color='white', key='uf', size=(4, 1))],
        [sg.Input(font='arial 12 bold', background_color='white', key='ddd', size=(4, 1))]
    ]

    botoes = [
        [
         sg.Button('Voltar', font='arial 12', size=(8, 1)),
         sg.Text(' ' * 5),
         sg.CButton('Sair', font='arial 12', size=(8, 1))]
    ]

    layout = [
        [sg.Text('Consultar o CEP (Código de Endereçamento Postal)', font='arial 18 bold', pad=(0, 0))],
        [sg.Column(cep, justification='center', element_justification='center')],
        [sg.Column(coluna1, pad=((0, 20), 0)), sg.Column(coluna2)],
        [sg.Column(botoes, justification='center')]
    ]
    telaCep = sg.Window('Consultar o CEP', element_padding=(0, 10), layout=layout, size=(800, 500),
                        finalize=True)


def tela_ddd():
    """
     Cria a janela de consulta DDD e suas configurações.
    Return: Sem retorno.
    """
    sg.theme('Reddit')

    ddd = [
        [sg.Text('Digite o DDD (Digite apenas 2 números)', font='arial 12', pad=(0, 0))],
        [sg.Input(size=(3, 0), font='arial 12', pad=(0, 0), key='ddd', background_color='white')],
        [sg.Button('Consultar', font='arial 12', size=(10, 1))]
    ]

    coluna1 = [
        [sg.Text('ESTADO:', font='arial 12')],
        [sg.Text('CIDADES:', font='arial 12', pad=(0, 95))],
    ]

    coluna2 = [
        [sg.Input(font='arial 12 bold', key='estado', size=(35, 1), background_color='white')],
        [sg.Output(font='arial 12 bold', key='cidades', size=(35, 10), background_color='white')],
    ]

    botoes = [
        [
         sg.Button('Voltar', font='arial 12', size=(8, 1)),
         sg.Text(' ' * 5),
         sg.CButton('Sair', font='arial 12', size=(8, 1))]
    ]

    layout = [
        [sg.Text('Consultar o DDD (Discagem Direta a Distância)', font='arial 18 bold', pad=(0, 0))],
        [sg.Column(ddd, justification='center', element_justification='center')],
        [sg.Column(coluna1, pad=((0, 20), 0)), sg.Column(coluna2)],
        [sg.Column(botoes, justification='center')]


    ]
    teladdd = sg.Window('Consultar o DDD', element_padding=(0, 10), layout=layout, size=(800, 500), finalize=True)


