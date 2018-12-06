from No import No

class Lista:
    def __init__(self):
        self.inicial = None
        self.final = None
        self.quantidade_itens = 0
        self.lista_indexada = False


    def append(self, valor):
        if self.inicial is None and self.final is None:
            """
            no = No(valor)
            self.inicial = no
            self.final = no
            """
            self.inicial = self.final = No(valor)
        else:
            # final aponta para o novo nó (Próximo final)
            self.final.proximo = no = No(valor)
            no.anterior = self.final
            self.final = self.final.proximo
        self.quantidade_itens += 1



    def pesquisa(self, valor):
        if self.lista_indexada == False:
            print("Calculo de saltos!")


            contador = 0
            salto = self.quantidade_itens
            while True:
                salto //= 2
                print(salto)
                if salto % 3 == 0:
                    contador -= 1
                if salto % 2 == 0:
                    contador += 1


            iterador = self.inicial
            cont = 0
            l = []
            while iterador is not None:
                if (cont % salto) == 0:
                    l.append(iterador)
                cont += 1
                iterador = iterador.proximo

            for i in l:
                print(i)

            # print("="*89)
            for i, item in enumerate(l):
                if i == 0:
                    self.inicial.salto = item
                else:
                    anterior.salto = item
                    # print("*"+str(item))
                anterior = item
                # print(anterior)
            self.lista_indexada = True

        # print("="*89)
        # iterador = self.inicial
        # while iterador is not None:
        #     print(f"{str(iterador)} -> Salto: {iterador.salto}")
        #     iterador = iterador.proximo

        iterador = self.inicial.salto
        while iterador is not None:
            # if iterador.salto is not None:
            #     print(f"{str(iterador.dado)} -> Salto: {iterador.salto.dado}")

            if valor < iterador.dado:
                print(f"{valor} <  {str(iterador.dado)} = {valor < iterador.dado}")
                if valor == iterador.anterior.dado:
                    print(f"{str(iterador.anterior.dado)} ==  {valor} = {valor == iterador.anterior.dado}")
                    break
                if valor is not iterador.anterior.dado:

                    iterador_volta = iterador.anterior
                    while iterador_volta.anterior:
                        if valor == iterador_volta.dado:
                            print(f"{str(iterador_volta.dado)} ==  {valor} = {valor == iterador_volta.dado}")
                            break

                        iterador_volta = iterador_volta.anterior
                    break
            if valor == iterador.dado:
                print(f"{str(iterador.dado)} ==  {valor} = {valor == iterador.dado}")
                break

            iterador = iterador.salto




    def __str__(self):
        iterador = self.inicial
        texto = "Lista: \n"
        while iterador is not None:
            texto += str(iterador)+"\n"
            iterador = iterador.proximo
        return texto
