class Rebatedor (Retangulo):
        def move-direita(self,width):
            x,y,w,-=self.bounds()
            x+=5 -> x.=5
            if x +w > width - w
            self.posicao=(x,y)

            for evento in pygame.event.get():
                if evento==pygame.KEYDWN:
                    if evento.key = pygame.K_RIGTH:
                        rebatedor.move-direita()
                    elif evento.key=pygame.K_LEFT:
                        rebatedor.move-esquerda()

        def move-esquerda
