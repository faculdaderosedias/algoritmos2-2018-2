"""Implementacao de Deque para prova de Algoritmos 2."""

class Deque:
    """Implementa um TAD para Deque."""

    def __init__(self, tamanho=5):
        """Inicializa um objeto Deque."""
        self._dados = [None] * tamanho
        self._head = 0
        self._tail = 0

    def empty(self):
        """Verifica se a Deque esta vazia."""
        return self._tail == self._head

    def full(self):
        """Verifica se a Deque esta cheia."""
        return self._proximo(self._tail) == self._head

    def capacity(self):
        """Verifica capacidade do Deque."""
        return len(self._dados)

    def pushBack(self, valor):
        """Insere no fim do Deque."""
        if not self.full():
            self._dados[self._tail] = valor
            self._tail = self._proximo(self._tail)

    def pushFront(self, valor):
        """Insere no fim do Deque."""
        if not self.full():
            posicao = self._anterior(self._head)
            self._dados[posicao] = valor
            self._head = posicao

    def _proximo(self, valor):
        return (valor + 1) % len(self._dados)

    def _anterior(self, valor):
        if valor == 0:
            return len(self._dados) - 1
        return valor - 1

    def peekFront(self):
        """Consulta o elemento na frente do Deque."""
        if not self.empty():
            return self._dados[self._head]

    def peekBack(self):
        """Consulta o elemento no final do Deque."""
        if not self.empty():
            return self._dados[self._tail - 1]

    def popBack(self):
        """Remove o ultimo elemento."""
        if not self.empty():
            self._tail = self._anterior(self._tail)
            return self._dados[self._tail]

    def popFront(self):
        """Remove o primeiro elemento."""
        if not self.empty():
            valor = self._dados[self._head]
            self._head = self._proximo(self._head)
            return valor
