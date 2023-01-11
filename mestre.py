import PySimpleGUI as sg

def f_mestre():
    layout = [
        [sg.Text('Cálculo Numérico')],
        [sg.Output(size=(60, 20), font='Times 12 bold')],
        [sg.Text('Digite a opção:')],
        [sg.Input(key='-escolha-', do_not_clear=True,size=(30,2))],
        [sg.Button('Seguir', bind_return_key=True)]

    ]

    window = sg.Window('Cálculo Numérico', layout)


    event = 0

    while True:

        event, values = window.read()

        # Obtém os valores digitados pelo usuário
        escolha = values['-escolha-']

        if event == 'Seguir' and escolha == '1':
            from loc_zeros import f_loc_zeros
            f_loc_zeros()

        if event == 'Seguir' and escolha == '2':
            from bissecao import f_bissecao
            f_bissecao()


        if event == 'Seguir' and escolha == '3':
            from ponto_fixo import f_ponto_fixo
            f_ponto_fixo()

        if event == 'Seguir' and escolha == '4':
            from secante import f_secante
            f_secante()

        if event == 'Seguir' and escolha == '5':
            from newton import f_newton
            f_newton()

while True:
    f_mestre()
