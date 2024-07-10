import os

def numero_par_impar():
    numero = int(input('Informe um número: \n'))

    if numero % 2 == 0:
        os.system('cls')
        print('O número é par\n')
    else:
        os.system('cls')
        print('O número é impar\n')

def idade():
    idade = int(input('Qual a sua idade: '))

    if idade >= 0 and idade <= 12:
        print('Criança\n')
    elif idade >= 13 and idade <= 18:
        print('Adolescente\n')
    elif idade > 18:
        print('Adulto\n')
    else:
        print('Idade invalida\n')

def plano_carteziano():
    x = int(input('Informe o valor de X: '))
    y = int(input('Informe o valor de y: '))

    if x > 0 and y > 0:
        print('Primeiro Quadrante')
    elif x < 0 and y > 0:
        print('Segundo Quadrante')
    elif x < 0 and y < 0:
        print('Terceiro Quadrante')
    elif x > 0 and y < 0:
        print('Quarto Quadrante')
    else:
        print('O ponto está localizado no eixo')

numero_par_impar()
idade()
plano_carteziano()