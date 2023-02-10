'''
Programa geral para esboçar gráficos de diversas funções com vários formatos de linha e cores além da inserção de
informações em locais específicos. Recomendamos o uso do PyCharm para a compilação deste programa.

RODANDO A PRIMEIRA VEZ (no PyCharm)
- No terminal instale os modulos, PySimpleGUI, webbrowser, os, numpy (e mais alguma se eu esqueci - aparecerá como
erro acusando a falta do módulo). Para instalar digite 'pip install PySimpleGUI',...

GERANDO UM EXECUTÁVEL .EXE (PyCharm)
- No terminal digite:
   - pip install pyinstaller
   - pyinstaller --onefile grafico_geral_pysimplegui.py
- O arquivo exe encontra-se na pasta dist, no diretório onde o programa grafico_geral_pysimplegui fica salvo.
'''


import PySimpleGUI as sg
import matplotlib.pyplot as plt
from pylab import arange, annotate
from numpy import*
import webbrowser
import os

def plot_grafico(f1,a,b,titulo,r,dx,lx,ly,tipo,cor,note,x_note,y_note):

    f1 = f'{f1}*x/x'
    f = lambda x: eval(f1)

    try:
        f= eval('lambda x: ' + f1)
        f(1 / pi + e)
    except:
        sg.popup("Função Inválida.")
        return

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

    if titulo == '':
        titulo = ''
    else:
        try:
            titulo = str(titulo)
        except:
            sg.popup("Digite um título adequado.")
            return

    if r == '':
        r = 1
    else:
        try:
            r = float(r)
        except:
            sg.popup("Digite a escala adequada.")
            return

    if dx == '':
        dx = 10**(-2)/(b-a)
    else:
        try:
            dx = float(dx)
        except:
            sg.popup("Digite o salto adequadamente.")
            return

    x = arange(a,b + dx,dx+0.00000000000001)
    y = f(x)

    try:
        tipo = str(tipo)
    except:
        sg.popup("Digite uma opção de tipo de gráfico válida, entre 1 e 8 ou deixe em branco.")
        return

    if tipo not in ['','1','2','3','4','5','6','7','8']:
        sg.popup("Digite uma opção de tipo de gráfico válida, entre 1 e 8 ou deixe em branco.")
        return

    if tipo == '' or tipo == '1':
        tipo = '-'
    elif tipo == '2':
        tipo = '-.'
    elif tipo == '3':
        tipo = ':'
    elif tipo == '4':
        tipo = '.'
    elif tipo == '5':
        tipo = 'o'
    elif tipo == '6':
        tipo = '*'
    elif tipo == '7':
        tipo = '+'
    elif tipo == '8':
        tipo = 'x'

    try:
        cor = str(cor)
    except:
        sg.popup("Digite uma opção de cor válida, entre 1 e 7 ou deixe em branco.")
        return

    if cor not in ['','1','2','3','4','5','6','7']:
        sg.popup("Digite uma opção de tipo de gráfico válida, entre 1 e 7 ou deixe em branco.")
        return

    if  cor == '' or cor == '1':
        cor = 'k'
    elif cor == '2':
        cor = 'b'
    elif cor == '3':
        cor = 'r'
    elif cor == '4':
        cor = 'g'
    elif cor == '5':
        cor = 'y'
    elif cor == '6':
        cor = 'c'
    elif cor == '7':
        cor =  'm'

    plt.plot(x,y,cor+tipo)
    plt.axhline(y=0, color="black", linestyle="-",linewidth=0.5)
    plt.axvline(x=0, color="black", linestyle="-",linewidth=0.5)
    axes = plt.gca()
    axes.set_aspect(r, adjustable='datalim')


    try:
        x_note = str(x_note)
    except:
        sg.popup("Digite uma entrada válida de abscissa de onde quer a informação.")
        return

    try:
        y_note = str(y_note)
    except:
        sg.popup("Digite uma entrada válida de ordenada de onde quer a informação.")
        return


    if x_note != '':
        x_note = float(x_note)
        if y_note == '':
            annotate(note, xy=(x_note, f(x_note)), xytext=(x_note, f(x_note)))
        else:
            y_note = float(y_note)
            annotate(note, xy=(x_note, y_note), xytext=(x_note, y_note))


    if lx == '':
        plt.xlabel('x')
    else:
        plt.xlabel(str(lx))
    if ly == '':
        plt.ylabel('y')
    else:
        plt.ylabel(str(ly))

    if k == 0:
        plt.grid(0.1)
    if titulo != '':
        plt.title(str(titulo))
    plt.show()


################################################CONSTRUINDO A INTERFACE################################################

layout = [
        [sg.Text('f(x)'), sg.Input(key='-f1-', do_not_clear=True, size=(28, 1)), sg.Button('?',key = '?1', bind_return_key=True),
         sg.Text('Extremos   a:'), sg.Input(key='-a-', do_not_clear=True, size=(10, 1)),
         sg.Text('b:'), sg.Input(key='-b-', do_not_clear=True, size=(10, 1)), sg.Button('?',key = '?2', bind_return_key=True),],
        [sg.Text('\n------------------------------------------------------- Opcionais -------------------------------------------------------')],
        [sg.Text('Título'),sg.Input(key='-titulo-', do_not_clear=True, size=(75, 1))],
        [sg.Text('dx:'), sg.Input(key='-dx-', do_not_clear=True, size=(10, 1)), sg.Button('?',key = '?3', bind_return_key=True),
         sg.Text('r:'), sg.Input(key='-r-', do_not_clear=True, size=(10, 1)), sg.Button('?',key = '?4', bind_return_key=True),],
        [sg.Text('Rótulos   x:'), sg.Input(key='-lx-', do_not_clear=True, size=(30, 1)),
         sg.Text('y: '),sg.Input(key='-ly-', do_not_clear=True, size=(30, 1)), sg.Button('?',key = '?5', bind_return_key=True),],
         [sg.Text('Tipo (1 a 8):'),sg.Input(key='-tipo-', do_not_clear=True, size=(2, 1)), sg.Button('?',key = '?6', bind_return_key=True),
          sg.Text('Cor (1 a 7):'),sg.Input(key='-cor-', do_not_clear=True, size=(2, 1)), sg.Button('?',key = '?7', bind_return_key=True),],
         [sg.Text('Destaque:'),sg.Input(key='-note-', do_not_clear=True, size=(30, 1)),
          sg.Text('x:'),sg.Input(key='-x_note-', do_not_clear=True, size=(10, 1)),
          sg.Text('y:'),sg.Input(key='-y_note-', do_not_clear=True, size=(10, 1)), sg.Button('?',key = '?8', bind_return_key=True)],
        [sg.Button('Esboçar', bind_return_key=True),
         sg.Button('Código', bind_return_key=True), sg.Button('Vídeo(Tutorial)', bind_return_key=True) ],
        [sg.Button('Sair', bind_return_key=True)],
        [sg.Text('Autoria: Allan de Sousa Soares\n'
                 'Professor do Instituto Federal de Educação,'
                 'Ciência e Tecnologia da Bahia, Campus Vitória da Conquista.',font='defalut 9')],

    ]

window = sg.Window('Esboço Gráfico by @prof_allanIFBA (youtube)', layout)

event = 0

while event != 'Sair':

        event, values = window.read()

        f1 = values['-f1-']
        a = values['-a-']
        b = values['-b-']
        titulo = values['-titulo-']
        r = values['-r-']
        dx = values['-dx-']
        lx = values['-lx-']
        ly = values['-ly-']
        tipo = values['-tipo-']
        cor = values['-cor-']
        note =  values['-note-']
        x_note = values['-x_note-']
        y_note = values['-y_note-']

        k=0
        if event == 'Esboçar':
            plot_grafico(f1,a,b,titulo,r,dx,lx,ly,tipo,cor,note,x_note,y_note)
            plt.grid()
            k = k+1

        if event == 'Código':
            os.system("start \"\" https://github.com/Allanifba/matematicacompython/blob/main/grafico_geral_pysimplegui.py")

        if event == 'Vídeo-Tutorial':
            os.system("start \"\" ")

        if event == '?1':
            sg.popup("A função digitada está incorreta, entre por exemplo com:\n"
                     "2*x + 1 para f(x) = 2x + 1\n"
                     "2*x**3-4 para f(x) = 2x^3-4\n"
                     "exp(2*x) para e^(2x)\n"
                     "sin(x) para sen(x)\n")

        if event == '?2':
            sg.popup("Valores correspondentes ao intervalo de esboço do gráfico. Digite valores reais.")

        if event == '?3':
            sg.popup("Valor correspondente à variação entre as abscissas. Geralmente apropriado para gráficos"
                     "do tipo 4 a 8 (veja abaixo). Deixando em branco, dx é entendido como 0.01*(b-a).\n"
                     "[] Para entender melhor, tome a função x**2 com a = -2 e b = 2. Incialmente deixe a entrada"
                     "correspondent ao tipo em branco. Depois, feche a janela do gráfico (para evitar sobreposição),"
                     "e escolha, por exemplo, a entrada 4 para o tipo.")

        if event == '?4':
            sg.popup("Valor correspondente achatamente do gráfico. Valores entre 0 e 1 'achatam' o eixo y"
                     "enquanto que valores maiores que 1 o 'esticam'.\n"
                     "[] Para entender melhor tome a função "
                     "x**2 com a = -2 e b = 2. Use para r valores 0.1, 0.5, 2 e 4. Deixando em branco, "
                     "r é entendido como 1.")

        if event == '?5':
            sg.popup("Adiciona rótulos nos eixos. Por exemplo, x pode representar o Tempo(s) e y a Temperatura(k). "
                     "Se deixado em branco entende-se que o rótulo do eixo-x é x e do eixo-y é y.")

        if event == '?6':
            sg.popup("Formata a linha do gráfico.\n"
                     "[] Se deixado em branco ou digitado 1, teremos uma linha contínua (-).\n"
                     "[] Para a entrada 2, tem-se uma linha ponto-traço (.-)\n"
                     "[] Para a entrada 3, tem-se uma linha pontilhada (.)\n"
                     "[] Para a entrada 4, tem-se uma linha pontilhada com pontos maiores(o) ou grossa a depender de dx\n"
                     "[] Para a entrada 5, tem-se uma linha pontilhada com pontos grandes(O) ou grossa a depender de dx\n"
                     "[] Para a entrada 6, tem-se uma linha pontilhada com pontos estrelados(*) ou grossa a depender de dx\n"
                     "[] Para a entrada 7, tem-se uma linha pontilhada com pontos em cruz(+) ou grossa a depender de dx\n"
                     "[] Para a entrada 8, tem-se uma linha pontilhada com pontos em xis(x) ou grossa a depender de dx\n")

        if event == '?7':
            sg.popup("Formata a cor do gráfico.\n"
                     "[] Se deixado em branco ou digitado 1, teremos a cor preta.\n"
                     "[] Para a entrada 2, tem-se a cor azul.\n"
                     "[] Para a entrada 3, tem-se a cor vermelha.\n"
                     "[] Para a entrada 4, tem-se a cor verde.\n"
                     "[] Para a entrada 5, tem-se a cor amarela.\n"
                     "[] Para a entrada 6, tem-se a cor ciano.\n"
                     "[] Para a entrada 7, tem-se a cor magenta\n")

        if event == '?8':
            sg.popup("Destaca, com uma palavra ou símbolo certa posição do gráfico.\n"
                     "[] Por exemplo, digite a função -x**2 com a = -2 e b = 2. No campo 'Destaque' insira Max e"
                     "nos campos x e y insira, respectivamente, -0.1 e -0.2. Requer prática acertar o local "
                     "adequado do destaque...")


window.close()
