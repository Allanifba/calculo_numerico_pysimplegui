import PySimpleGUI as sg
from numpy import*

def f_newton():

#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################
    def newton(f,df,p0,tol):
        i = 0
        F = lambda x: eval(f)
        DF = lambda x: eval(df)
        delta = float('inf')

        if DF(p0) != 0:
            i = 0
            delta = float('inf')

            print(f'Note que f(x) = {f} contínuam em [a,b] e diferenciável em (a,b) com f´(x) = {df} não nula em '
                  f'neste aberto. Portanto o método de Newton pode ser aplicado. A tabela a seguir mostra as '
                  f'iterações e o erro:')
            print('                      n                pn                            en')
            while tol < delta:
                p = p0 - F(p0) / DF(p0)
                i = i + 1
                delta = abs(p0 - p)
                print(f'                      %0.0f   %0.13f    %0.13f' % (i, p, delta))
                p0 = p
        return print(f'Resultado: {p}')

################################################CONSTRUINDO A INTERFACE################################################

    layout = [
        [sg.Text('Método de Newton')],
        [sg.Output(size=(60, 20), font='Times 12 bold')],
        [sg.Text('Digite a função f:')],
        [sg.Input(key='-f-', do_not_clear=True,size=(30,2))],
        [sg.Text('Digite a derivada de f:')],
        [sg.Input(key='-df-', do_not_clear=True,size=(10,1))],
        [sg.Text('Digite o valor inicial p0:')],
        [sg.Input(key='-p0-', do_not_clear=True,size=(10,1))],
        [sg.Text('Digite a tolerância:')],
        [sg.Input(key='-tol-', do_not_clear=True,size=(10,1))],
        [sg.Button('Calcular', bind_return_key=True)],
        [sg.Button('Voltar', bind_return_key=True)]

    ]

    window = sg.Window('Método de Newton', layout)


    event = 0

    while event != 'Voltar':

        event, values = window.read()
        f = values['-f-']
        df = values['-df-']
        p0 = values['-p0-']
        tol = values['-tol-']

        if event == 'Calcular' and (values['-f-'] == '' or
                                    values['-df-'] == '' or
                                    values['-p0-'] == '' or
                                    values['-tol-'] == '' ):
           print('Preencha todos os campos!\n')

        else:
            p0 = float(p0)
            tol = float(tol)
            newton(f, df, p0, tol)

    window.close()

