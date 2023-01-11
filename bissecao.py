import PySimpleGUI as sg
from numpy import*

def f_bissecao():

#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################
    def bissecao(f,a,b,tol):
        i = 0
        F = lambda x: eval(f)
        delta = float('inf')

        if F(a) * F(b) > 0:
            return print(f'O método da bisseção não pode ser aplicado a f(x) = {f} no intervalo [{a},{b}], pois '
                     f'f({a}) = {F(a)} e f({b}) = {F(b)} têm sinais iguais.\n')

        else:
            print(f'Note que f(x) = {f} é tal que f({a}) = {F(a)} e f({b}) = {F(b)}. Portanto f satisfaz a condição '
                  f'f(a)*f(b) < 0. Sendo f contínua no intervalo [{a},{b}], temos que o método da bissecção pode ser '
                  f'aplicado a este intervalo. A tabela a seguir mostra as iterações e o erro.')

            # Exibe os elementos do título da tabela
            print('                      n               pn                            en')

            while tol < delta:
                Fa = F(a)
                p = (a + b) / 2
                i = i + 1
                delta = abs(p - a)
                print(f'                      %0.0f   %0.13f    %0.13f' % (i, p, (b - a) / 2))
                if F(a) * F(p) < 0:
                    b = p
                else:
                    a = p
            return print(f'Resultado: {p} \n')


################################################CONSTRUINDO A INTERFACE################################################

    layout = [
        [sg.Text('Método da Bisseção')],
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

    window = sg.Window('Método da Bisseção', layout)


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
            bissecao(f, a, b, tol)

    window.close()





