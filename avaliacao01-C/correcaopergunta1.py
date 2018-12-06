from ball import ballimport pygame

pygame.init()
width,height=size=(400,400)
screen=pygame.dysplay.set_mode(size)
speadx,speedy=5,5
    def verifica_limites_tela (circulo):
        x,y = circulo.centro
        r = circulo.raio
        //esquerda
        if x+r>=whidth or x-r<=0
        spedx *=-1
        bola.troca-cor()

        //direita
        if y++>=heigth or y-r<=0:
            sped*-1
            bola.troca-cor()

        //tratar eventos
        //atualizar dados
        //desenhar
        //update

        clock.tick(30)
        pygame.dyplay.flip()
        verificar-limites-tela(ball)
        ball.more(speedx, spedy)
        pygame.draw(screen)

        if borda esquerda
        if borda superior
        if borda inferior

        if y++ >= heigth or y-r <=0
        speedy *=-1
        bola.troca-cor()

    def troca-cor(self):
        cores=[(255,0,0),
        (0,255,0),
        (0,0,255),
        (255,255,0),
        (255,0,255),
        (0,255,255)]

    self.cor=random.choice(cores)
