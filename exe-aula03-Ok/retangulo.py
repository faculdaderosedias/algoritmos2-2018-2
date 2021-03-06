#Implementar uma função, utilizando a linguagem python,
#que verifica a colisão de dois retângulos.
#Implemente o código de testes utilizando o arquivo de funcionalidade em anexo.

"""Define uma classe Retangulo com colisao."""

class Retangulo:
    """Define objetos do tipo retangulo."""

    def __init__(self, x, y, w, h):
        """Inicializa objeto retangulo."""
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def colide(self, ponto):
        """Testa se um ponto colide com este retangulo."""
        x = ponto[0]
        y = ponto[1]
        if x < self.x or x > self.x + self.width:
            return False
        if y < self.y or y > self.y + self.height:
            return False
        return True
