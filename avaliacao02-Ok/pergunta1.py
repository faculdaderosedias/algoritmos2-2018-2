#Dada uma linguagem de programação que tem apenas três comandos:
#atibuição: =
#repetição: while
#teste: if - else
#E duas classes para organização dos dados,
#a Pilha e a Fila, sendo que as duas classes possuem os mesmos métodos públicos:
#push(valor) - Insere um valor na estrutura;
#pop(): valor - Retira um valor da estrutura;
#peek(): valor - Mostra o próximo valor a ser retirado;
#empty(): boolean - Verifica se a estrutura está vazia.
#Crie uma função que recebe uma
#Fila como parametro (def inverte(fila)) e inverte a ordem dos elementos na fila.##

class Pilha:
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

        def push(self, item) :
            self.items.apend(item)
            def pop(self) :
                return self.items.pop()
                def isEmpty(self) :
                    return (self.items == [])

class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo   = None
        def __repr__(self):
            return "[" + str(self.primeiro) + "]"
            def push(self, item) :
                self.items.apend(item)
                def pop(self) :
                    return self.items.pop()
                    def isEmpty(self) :
