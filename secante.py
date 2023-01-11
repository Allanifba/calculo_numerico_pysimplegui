import PySimpleGUI as sg
from numpy import*

def f_secante():

#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################
    def secante(f, a, b, tol):
        F = lambda x: eval(f)
        if F(a) * F(b) < 0:
            i = 1
            s0 = F(a)
            s1 = F(b)
            delta = float('inf')
            print(f'Note que f(x) = {f} contínuam em [{a},{b}] e diferenciável em ({a},{b}) com f´(x) não nula em '
                  f'neste aberto. Portanto o método da secante pode ser aplicado. A tabela a seguir mostra as '
                  f'iterações e o erro:')
            print('                      n          pn                en')
            while tol < delta:
                p = b - s1 * (b - a) / (s1 - s0)
                i = i + 1
                delta = abs(b - p)
                a = b
                s0 = s1
                b = p
                s1 = F(p)
                print(f'                      %0.0f   %0.13f    %0.13f' % (i, p, delta))
            return print(f'Resultado: {p}')

################################################CONSTRUINDO A INTERFACE################################################

    layout = [
        [sg.Text('Método da Secante')],
        [sg.Output(size=(60, 20), font='Times 12 bold')],
        [sg.Text('Digite a função:')],
        [sg.Input(key='-f-', do_not_clear=True,size=(30,2))],
        [sg.Text('Digite o extremo inferior do intervalo:')],
        [sg.Input(key='-a-', do_not_clear=True,size=(10,1))],
        [sg.Text('Digite o extremo superior do intervalo:')],
        [sg.Input(key='-b-', do_not_clear=True,size=(10,1))],
        [sg.Text('Digite a tolerância:')],
        [sg.Input(key='-tol-', do_not_clear=True,size=(10,1))],
        [sg.Button('Calcular', bind_return_key=True)],
        [sg.Button('Voltar', bind_return_key=True)]

    ]

    window = sg.Window('Método da Secante', layout)


    event = 0

    while event != 'Voltar':

        event, values = window.read()
        f = values['-f-']
        a = values['-a-']
        b = values['-b-']
        tol = values['-tol-']

        if event == 'Calcular' and (values['-f-'] == '' or
                                    values['-a-'] == '' or
                                    values['-b-'] == '' or
                                    values['-tol-'] == '' ):
           print('Preencha todos os campos!\n')

        else:
            a = float(a)
            b = float(b)
            tol = float(tol)
            secante(f, a, b, tol)

    window.close()
