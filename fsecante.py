from numpy import*

#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################
def secante(f,a,b,tol):
    F = lambda x: eval(f)
    if F(a) * F(b) < 0:
        i = 1
        s0 = F(a)
        s1 = F(b)
        delta = float('inf')

        print(f'Note que f(x) = {f} contínuam em [{a},{b}] e diferenciável em ({a},{b}) com f´(x) não nula em \n'
              f'neste aberto. Portanto o método da secante pode ser aplicado. A tabela a seguir mostra as \n'
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

'''
Exemplo: secante('x**2-4',0,5,0.01)
'''
