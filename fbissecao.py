from numpy import*

#############################################DEFININDO A FUNÇÃO DE ITERAÇÃO#############################################

def bissecao(f,a,b,tol):
    i = 0
    F = lambda x: eval(f)
    delta = float('inf')

    if F(a) * F(b) > 0:
        return print(f'O método da bisseção não pode ser aplicado a f(x) = {f} no intervalo [{a},{b}], pois \n'
                     f'f({a}) = {F(a)} e f({b}) = {F(b)} têm sinais iguais.')

    else:
        print(f'Note que f(x) = {f} é tal que f({a}) = {F(a)} e f({b}) = {F(b)}. Portanto f satisfaz a condição \n'
              f'f(a)*f(b) < 0. Sendo f contínua no intervalo [{a},{b}], temos que o método da bissecção pode ser \n'
              f'aplicado a este intervalo. A tabela a seguir mostra as iterações e o erro.')

        # Exibe os elementos do título da tabela
        print('                      n           pn               en')

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
        return print(f'Resultado: {p}')

'''
Exemplos: 
bissecao('x**2-2',0,2,0.01) (aplicável)
bissecao('x**2-2',0,1,0.01) (não aplicável)
'''
