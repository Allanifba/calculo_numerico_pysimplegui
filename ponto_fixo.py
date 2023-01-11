import PySimpleGUI as sg
from numpy import*

def f_ponto_fixo():

#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################
    def ponto_fixo(g, p0, tol):
        G = lambda x: eval(g)
        i = 0
        delta = float('inf')
        print(
            f'Note que g([a,b]) está contida em [a,b] com p0 = {p0} neste intervalo e |g´(x)| <= k < 1 para todo x em '
            f'(a,b). Portanto, o método do ponto fixo pode ser aplicado. A tabela a seguir mostra as iterações e o erro:')
        print('                      n               pn                            en')
        while tol < delta:
            p = G(p0)
            i = i + 1
            delta = abs(p0 - p)
            print(f'                      %0.0f   %0.13f    %0.13f' % (i, p, delta))
            p0 = p
        return print(f'Resultado: {p}')
################################################CONSTRUINDO A INTERFACE################################################

    layout = [
        [sg.Text('Método do Ponto Fixo')],
        [sg.Output(size=(60, 20), font='Times 12 bold')],
        [sg.Text('Digite a função:')],
        [sg.Input(key='-g-', do_not_clear=True,size=(30,2))],
        [sg.Text('Digite o valor inicial p0:')],
        [sg.Input(key='-p0-', do_not_clear=True,size=(10,1))],
        [sg.Text('Digite a tolerância:')],
        [sg.Input(key='-tol-', do_not_clear=True,size=(10,1))],
        [sg.Button('Calcular', bind_return_key=True)],
        [sg.Button('Voltar', bind_return_key=True)]

    ]

    window = sg.Window('Método do Ponto Fixo', layout)


    event = 0

    while event != 'Voltar':

        event, values = window.read()
        g = values['-g-']
        p0 = values['-p0-']
        tol = values['-tol-']

        if event == 'Calcular' and (values['-g-'] == '' or
                                    values['-p0-'] == '' or
                                    values['-tol-'] == '' ):
           print('Preencha todos os campos!\n')

        else:
            p0 = float(p0)
            tol = float(tol)
            ponto_fixo(g, p0, tol)


    window.close()