#Crie um programa que inicie uma janela no tamanho 800 x 600,
#com o título "PyGame Tutorial", e encerre o programa ao teclar "ESC".

from pygame import *
from sys import exit

class Main:
    def criar_janela(self):
        while True:
            for evento in event.get():
                if evento.type == QUIT:
                    exit()
                if evento.type == KEYDOWN and evento.key == K_ESCAPE:
                    exit()

            display.flip()

    def __init__(self):
        init()

        self.tamanho = self.largura, self.altura = 800, 600

        self.janela = display.set_mode(self.tamanho)
        display.set_caption(PyGame Tutorial!")

        self.criar_janela()

if __name__ == '__main__':
    Main()
