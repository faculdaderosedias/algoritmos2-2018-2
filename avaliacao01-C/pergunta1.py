#Crie uma classe Bola com os campos: centro, raio e cor.
#Crie um programa que mostre uma janela com 400 x 400 pixels,
#onde a bola fica batendo nos limites da janela, trocando de cor e invertendo a direção cada vez que bater nos limintes.
#Por exemplo, ao bater no limite esquerdo da janela,
#a bola passará a mover-se para a direita,
#ao bater no limite superior, passará a mover-se para baixo.
import pygame

class Bola:
    def __init__(self, centro, raio, cor):
        self.centro = centro #circunf.
        self.raio = raio
        self.cor = cor

class Retangulo:

    def __init__(self, x, y, w, h):

        self.centro = x
        self.raio = y
        self.cor = z
        self.width = 400
        self.height = 400

    def colide(self, ponto):

        x = centro[0]
        y = raio[1]
        if x < self.x or x > self.x + self.width:
            return False
        if y < self.y or y > self.y + self.height:
            return False
        return True
