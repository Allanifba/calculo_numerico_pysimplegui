from numpy import*


#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################
def ponto_fixo(g, p0, tol):
    G = lambda x: eval(g)
    i = 0
    delta = float('inf')
    print(f'Note que g([a,b]) está contida em [a,b] com p0 = {p0} neste intervalo e |g´(x)| <= k < 1 para todo x em \n'
          f'(a,b). Portanto, o método do ponto fixo pode ser aplicado. A tabela a seguir mostra as iterações e o \n'
          f'erro:')
    print('                      n          pn                en')
    while tol < delta:
        p = G(p0)
        i = i + 1
        delta = abs(p0 - p)
        print(f'                      %0.0f   %0.13f    %0.13f' % (i, p, delta))
        p0 = p
    return print(f'Resultado: {p}')

'''
Exemplo: ponto_fixo('log(10/x)',1,0.01)
'''






