from numpy import*

#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################

def newton(f,df,p0,tol):
    i = 0
    F = lambda x: eval(f)
    DF = lambda x: eval(df)
    delta = float('inf')

    if DF(p0) != 0:
        i = 0
        delta = float('inf')

        print(f'Note que f(x) = {f} contínuam em [a,b] e diferenciável em (a,b) com f´(x) = {df} não nula em \n'
              f'neste aberto. Portanto o método de Newton pode ser aplicado. A tabela a seguir mostra as \n'
              f'iterações e o erro:')
        print('                      n          pn                 en')
        while tol < delta:
            p = p0 - F(p0) / DF(p0)
            i = i + 1
            delta = abs(p0 - p)
            print(f'                      %0.0f   %0.13f    %0.13f' % (i, p, delta))
            p0 = p
    return print(f'Resultado: {p}')

'''
Exemplo: newton('x**2-2','2*x',1,0.01)
'''