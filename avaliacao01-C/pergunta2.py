#Crie uma classe Retangulo, que contenha os compos: posição, largura, altura e cor. - Ok
#Crie um programa que utilize a classe Retângulo e mostre, em uma janela de 400 x 400 pixels,
# 6 linhas de 10 retângulos. Os retangulos devem ter 8 cores diferentes.
import pygame

class Retangulo:
    def __init__(self, posicao, largura, cor):
        self.posicao = posicao
        self.altura = altura
        self.cor = cor
        size = (400, 400)
        screen = pygame.display.set_mode(size)
                pygame.init()

    def oito_linhas():
        linha_quadrado()
        linha_quadrado()
        linha_quadrado()
        linha_quadrado()

    def Linha_quadrado():
        print( '+','- ' *8,'+', '- ' * 8, '+','- ' * 8, '+' ,'- ' * 8, '+')

    def linha_quadrado():
        print ('|', )

    def quadrado():
        Linha_quadrado()
        oito_linhas()
        Linha_quadrado()
        oito_linhas()
        Linha_quadrado()

        quadrado()
