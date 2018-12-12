#Criar uma classe ListaEncadeada, utilizando a linguagem Python, contendo os seguintes métodos:
#size(): retorna o número de elementos armazenados na lista. Ex.: i = lista.size()
#remove(X): remove todos os elementos com o valor X da lista. Ex.: lista.remove(5)
#append(X): adiciona o elemento X ao final da lista. Ex.: lista.append(5)
#addFirst(X): adiciona o elemento X no início da lista. Ex.: lista.addFirst(3)
#pop(): remove o elemento no final da lista e o retorna ao chamador. Ex.: i = lista.pop()
#removeFirst(): remove o elemento no início da lista. Ex.: lista.removeFirst()
#first(): retorna o primeiro elemento da lista. Ex.: iterador = lista.first()
#last(): retorna o ultimo elemento da lista. Ex.: iterador = iterador.last()
#O seguinte código deve funcionar com a lista:
#iterador = lista.first()
#while iterador is not None:
#    print(iterador.value)
#    iterador = iterador.next
class No:
    def __init__(self, valor):
        self.dado = valor
        self.proximo = None

    def __str__(self):
        if self.proximo is None:
            return f"Nó: {self.dado} | \tPróximo Nó: {self.proximo} \n"
        else:
            return f"Nó: {self.dado} | \tProximo Nó: {self.proximo.dado} \n"

class Lista:
    def __init__(self):
        self.inicial = None
        self.final = None
        self.tamanho = 0

    def last(self):
        return self.final

    def first(self):
        return  self.inicial

    def size(self):
        return self.tamanho

    def __len__(self):
        return  self.size()


    def append(self, valor):
        if self.final is None:
            self.inicial = self.final = No(valor)
        else:
            self.final.proximo = No(valor)
            self.final = self.final.proximo

    def addFirst(self, valor):
        no = No(valor)
        no.proximo = self.inicial
        self.inicial = no

    def removeFirst(self):
        self.inicial = self.inicial.proximo

    def removeLast(self):
        anterior = None
        iterador = self.inicial
        while iterador.proximo:
            if iterador.proximo is None:
                break
            anterior = iterador
            iterador = iterador.proximo
        anterior.proximo = None

    def pop(self):
        anterior = None
        iterador = self.inicial
        while iterador.proximo:
            if iterador.proximo is None:
                break
            anterior = iterador
            iterador = iterador.proximo
        anterior.proximo = None
        return iterador

    def remove(self, valor):
        iterador = self.inicial
        while iterador.proximo:
            if iterador.dado is valor:
                anterior.proximo = iterador.proximo
            anterior = iterador
            iterador = iterador.proximo

        if self.final.dado is valor:
            self.pop()
        elif self.inicial.dado is valor:
            self.removeFirst()

    def __str__(self):
        texto = ""
        iterador = self.inicial
        while iterador is not  None:
            texto += str(iterador)
            iterador = iterador.proximo
        return texto

if __name__ == '__main__':
    from random import  randint

    lista = Lista()

    for i in range(30):
        lista.append(randint(0, 10))

    print(str(lista))

    print("="*100)

    n = randint(0, 10)
    print(n)
    lista.remove(n)

    print(str(lista))
