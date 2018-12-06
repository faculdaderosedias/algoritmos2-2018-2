class Retangulo
    def __init__(self,x,y,w,h):
        self.posicao=(x,y)
        self.size=(w,h)
        self.cor=self.escolhe-cor()

    def draw(self,screen):
        pygame.draw.tec+(screen,self.cor,self.bounds())

        //cria lista de retangulos
        for ret in range(10):
            x +=31
            retangulo= Retangulo(x,y,30,15)
            retangulo.append(retangulo)
            x+=31
            y+=20
            x=45
        for ret in retangulos:
            ret.drw(screen)
