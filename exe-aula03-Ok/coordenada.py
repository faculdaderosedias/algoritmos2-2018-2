#Funcao em Python que que verifica:
# Se um ponto está dentro de um retângulo.
#Verificar se uma coordenada está dentro de um retângulo.
#Considerando os pontos
#A(x7;y8)
#B(x6;y7).

class Retangulo:
    def verif_dentro_ponto(self, pontos): """ponto dentro"""
        x, y = pontos
        if x < self.x or x > (self.x + self.larg):
            return False
        elif y < self.y or y > (self.y + self.alt):
            return False
        return True

    def __init__(self, x, y, larg, alt):"""valor de x,y larg e alt"""
        self.larg = larg
        self.alt = alt
        self.x = x
        self.y = y
