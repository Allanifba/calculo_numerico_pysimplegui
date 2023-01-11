import PySimpleGUI as sg
from numpy import*

def f_loc_zeros():

#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################

    def loc_zeros(f, a, b, n):
        a0 = a
        b0 = b
        gamma = (b - a) / n
        F = lambda x: eval(f)


        i = 0
        while a <= b:
            Fa = F(a)
            if Fa == 0:
                i = i + 1
                if i == 1:
                    print(f'Note que f(x) = {f} é contínua em [{a0},{b0}]. Portanto podemos aplicar o método de localização de zeros.')
                print(f'-Temos que {a} é um zero de f.')
            a = a + gamma
            Fc = F(a)
            if Fa * Fc < 0:
                i = i + 1
                if i == 1:
                    print(f'Note que f(x) = {f} é contínua em [{a0},{b0}]. Portanto podemos aplicar o método de localização de zeros.')
                print(f'-Existe ao menos um zero entre {a - gamma} e {a}.')
        if i != 0:
            print(' ')
        if i == 0:
            print(f'Note que f(x) = {f} é contínua em [{a0},{b0}]. Portanto podemos aplicar o método de localização de zeros. Contudo, '
                  f'não localizamos nenhum zero. \n')

################################################CONSTRUINDO A INTERFACE################################################

    layout = [
        [sg.Text('Método de Localização de Zeros')],
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
            loc_zeros(f, a, b, tol)

    window.close()
