#Inserir um numero em uma lista encadeada;
#manter ordenada;
from random import randint

class No:
    def __init__(self, valor=randint(0, 100)):
        self.dado = valor
        self.proximo = None

class Lista:
    def __init__(self):
        self.inicial = None
        self.final  = None

    def append(self, valor):
        if self.inicial is None and self.final is None:
            self.inicial = self.final = No(valor)
        else:
            self.final.proximo = No(valor)
            self.final = self.final.proximo
        self.organizar()

    def pop(self):
        if self.final is not None:
            iterador = self.inicial
            anterior  = None
            while iterador is not None:
                if iterador.proximo is None:
                    break
                anterior = iterador
                iterador = iterador.proximo
            aux = anterior.proximo
            anterior.proximo = None
            return aux
    def list(self):
        iterador = self.inicial
        while iterador is not None:
            print(iterador.dado)
            iterador = iterador.proximo

    def organizar(self):
        pass
        # iterador = self.inicial
        # while iterador is not None:
        #     if iterador is not None and iterador.proximo is not None and iterador.proximo.proximo is not None:
        #         if iterador.dado > iterador.proximo.dado and iterador.proximo.proximo.dado < iterador.proximo.dado:
        #             aux = iterador
        #             iterador.proximo  =  aux.proximo.proximo
        #             aux.proximo.proximo = iterador
        #
        #             print("#"*100)
        #     iterador = iterador.proximo

lista = Lista()
for i in range(10):
    lista.append(randint(0, 100))

lista.list()

print("#"*100)
print(lista.pop().dado)
print("#"*100)

lista.list()
