# Destaques pontuais no gráfico de uma função
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from pylab import arange, annotate
from numpy import*
import webbrowser
import os

def plot_grafico(f1,a,b,dx,lx,ly,t,c,x_note,y_note,ds):
    f1 = str(f1)

    try:
        a = float(a)
    except:
        sg.popup("Digite o extremo inferior corretamente.")
        return

    try:
        b = float(b)
    except:
        sg.popup("Digite o extremo superior corretamente.")
        return

    if dx == '':
        dx = 10**(-2)/(b-a)
    else:
        try:
            dx = float(dx)
        except:
            sg.popup("Digite o salto adequadamente.")
            return

    def f(x):
        return eval(f1)

    x = arange(a,b + dx,dx)
    try:
        y = f(x)
    except:
        sg.popup("Entrada 1 não é uma função")
        return

    try:
        t = str(t)
    except:
        sg.popup("Digite uma opção de tipo de gráfico válida, entre 1 e 8 ou deixe em branco.")
        return

    if t not in ['','1','2','3','4','5','6','7','8']:
        sg.popup("Digite uma opção de tipo de gráfico válida, entre 1 e 8 ou deixe em branco.")
        return

    if t == '' or t == '1':
        t = '-'
    elif t == '2':
        t = '-.'
    elif t == '3':
        t = ':'
    elif t == '4':
        t = '.'
    elif t == '5':
        t = 'o'
    elif t == '6':
        t = '*'
    elif t == '7':
        t = '+'
    elif t == '8':
        t = 'x'

    try:
        c = str(c)
    except:
        sg.popup("Digite uma opção de cor válida, entre 1 e 7 ou deixe em branco.")
        return

    if c not in ['','1','2','3','4','5','6','7']:
        sg.popup("Digite uma opção de tipo de gráfico válida, entre 1 e 7 ou deixe em branco.")
        return

    if  c == '' or c == '1':
        c = 'k'
    elif c == '2':
        c = 'b'
    elif c == '3':
        c = 'r'
    elif c == '4':
        c = 'g'
    elif c == '5':
        c = 'c'
    elif c == '6':
        c = 'm'
    elif c == '7':
        c =  'y'

    plt.plot(x,y,c+t)

    try:
        x_note = str(x_note)
    except:
        sg.popup("Digite uma entrada válida de abscissa de onde quer a informação.")
        return
    try:
        x_note = str(x_note)
    except:
        sg.popup("Digite uma entrada válida de ordenada de onde quer a informação.")
        return

    if x_note != '':
        x_note = float(x_note)
        if y_note == '':
            annotate(ds, xy=(x_note, f(x_note)), xytext=(x_note, f(x_note)))
        else:
            y_note = float(y_note)
            annotate(ds, xy=(x_note, y_note), xytext=(x_note, y_note))


    plt.title(f'Esboço Gráfico by @prof_allanIFBA')
    if lx == '':
        plt.xlabel('x')
    else:
        plt.xlabel(str(lx))
    if ly == '':
        plt.ylabel('y')
    else:
        plt.ylabel(str(ly))

    k = 0
    if k == 0:
        plt.grid()
        k=k+1
    plt.show()


################################################CONSTRUINDO A INTERFACE################################################

layout = [
        [sg.Text('Esboço Gráfico')],
        [sg.Text('f(x)'), sg.Input(key='-f1-', do_not_clear=True, size=(20, 1)),
         sg.Text('a: '), sg.Input(key='-a-', do_not_clear=True, size=(8, 1)),
         sg.Text('b: '), sg.Input(key='-b-', do_not_clear=True, size=(8, 1))],
        [sg.Text('Incrementos (opcionais): ')],
        [sg.Text('dx: '), sg.Input(key='-dx-', do_not_clear=True, size=(8, 1)),
         sg.Text('Rótulo-x: '), sg.Input(key='-lx-', do_not_clear=True, size=(15, 1)),
         sg.Text('Rótulo-y: '),sg.Input(key='-ly-', do_not_clear=True, size=(15, 1))],
         [sg.Text('Tipo (1 a 10): '),sg.Input(key='-t-', do_not_clear=True, size=(3, 1)),
          sg.Text('Cor (1 a 7): '),sg.Input(key='-c-', do_not_clear=True, size=(3, 1)),
          sg.Text('Destaque: '),sg.Input(key='-ds-', do_not_clear=True, size=(3, 1)),
          sg.Text('x: '),sg.Input(key='-x_note-', do_not_clear=True, size=(3, 1)),
          sg.Text('y: '),sg.Input(key='-y_note-', do_not_clear=True, size=(3, 1))],
        [sg.Button('Esboçar', bind_return_key=True),
         sg.Button('Código', bind_return_key=True)],
        [sg.Button('Sair', bind_return_key=True)]

    ]

window = sg.Window('Cálculo Numérico - youtube: @prof_allanIFBA', layout)

event = 0

while event != 'Sair':

        event, values = window.read()

        f1 = values['-f1-']
        a = values['-a-']
        b = values['-b-']
        dx = values['-dx-']
        lx = values['-lx-']
        ly = values['-ly-']
        t = values['-t-']
        c = values['-c-']
        ds = values['-ds-']
        x_note = values['-x_note-']
        y_note = values['-y_note-']

        k=0
        if event == 'Esboçar':
            plot_grafico(f1,a,b,dx,lx,ly,t,c,x_note,y_note,ds)
            plt.grid()
            k = k+1
        if event == 'Código':
            os.system("start \"\" https://github.com/Allanifba/calculo_numerico_pysimplegui")



window.close()

'''
    if x_note != '':
        x_note = float(x_note)
        if  y_note == '':
            annotate(ds, xy=(x_note, f(x_note)), xytext=(x_note, f(x_note)))
        else:
            y_note = float(y_note)
            annotate(ds, xy=(x_note, y_note), xytext=(x_note, y_note))
'''