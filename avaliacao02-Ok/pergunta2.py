#Deque é uma fila com inserção e remoção na duas pontas.
#Um deque pode ser implementado utilizando a técnica de buffer circular.
#Utilizando a linguagem Python e a ferramenta Behave, implemente uma classe Deque,
#com estrutura de armazenamento estática, e buffer circular.

#Crie os testes e o código para passar nos testes para a criação da estrutura,
#e inserção de elementos no fim da estrutura, baseados nos cenários disponíveis em
#https://bitbucket.com/rafasgj/prova_algoritmos2.git
#O método para inserção no fim deve ser pushBack(valor).
#O método de consulta do elemento na frente da estrutura deve ser peekFront().
#O método de consulta do elemento no final da estrutura de ser peekBack().
#O método de verificacao para saber se a estrutura está vazia de ser empty().
#O método de verificação para saber se a estrutura está cheia deve ser full().
#Devem ser implementados os cenários 1 a 4.

#Criar um Deque.
from collections import deque
    d = deque('10')
    for elem in d:
    print elem.pushBack()

    def is_empty(self):
        return len(self.__queue)==0

    def add(self,element):
        self.__queue.append(element)

    def full(self):
        if(self.is_empty()):
            raise(Empty('Queue is empty'))
        else:
            return self.__queue.pop(0)

    def peekBack(self):
        if(self.is_empty()):
            raise(Empty('Queue is empty'))
        else:
            return self.__queue[0]

if __name__ == '__main__':
    myQueue=Queue()
