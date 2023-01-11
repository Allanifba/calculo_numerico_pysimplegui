from numpy import*

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
                print(
                    f'Note que f(x) = {f} é contínua em [{a0},{b0}]. Portanto podemos aplicar o método de localização de zeros.')
            print(f'-Temos que {a} é um zero de f.')
        a = a + gamma
        Fc = F(a)
        if Fa * Fc < 0:
            i = i + 1
            if i == 1:
                print(
                    f'Note que f(x) = {f} é contínua em [{a0},{b0}]. Portanto podemos aplicar o método de localização \n'
                    f'de zeros.')
            print(f'-Existe ao menos um zero entre {a - gamma} e {a}.')
    if i != 0:
        print(' ')
    if i == 0:
        print(
            f'Note que f(x) = {f} é contínua em [{a0},{b0}]. Portanto podemos aplicar o método de localização de \n'
            f'zeros. Contudo, não localizamos nenhum zero. \n')

'''
Exemplos: 
loc_zeros('16*x**3-22*x-5',-2,2,8)
loc_zeros('x**2+5',0,4,10)
loc_zeros('x**2-4',-2,2,8)
loc_zeros('x**2-4',-2,3,8)
'''