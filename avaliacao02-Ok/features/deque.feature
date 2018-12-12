# language: pt

Funcionalidade: Implementar uma classe Deque.

# Cenario 1
Cenario: Criar um Deque.
  Dado o tamanho da estrutura sendo 10
  Quando crio um deque
  Entao tenho um deque com capacidade para armazenar 10 elementos
    E a estrutura esta vazia

# Cenario 2
Cenario: Inserir um valor no Deque.
  Dado que eu tenho um deque
  Quando insiro, no final da estrutura, o valor 8
  Entao a estrutura nao esta vazia
    E o elemento na frente da estrutura tem o valor 8

# Cenario 3
Cenario: Inserir mais de um valor no Deque.
  Dado que eu tenho um deque
  Quando insiro, no final da estrutura, os valores [1, 2, 3, 4]
  Entao a estrutura nao esta vazia
    E o elemento na frente da estrutura tem o valor 1
    E o elemento no final da estrutura tem o valor 4

# Cenario 4
Cenario: Inserir um valor  no Deque, com elementos.
  Dado que eu tenho um deque
    E este deque tem os elementos, inseridos no final, [1, 3, 5, 7]
  Quando insiro, no final da estrutura, o valor 9
  Entao a estrutura nao esta vazia
    E o elemento na frente da estrutura tem o valor 1
    E o elemento no final da estrutura tem o valor 9


    # Cenario 5
Cenario: Inserir um valor no início Deque.
  Dado que eu tenho um deque
  Quando insiro, no início da estrutura, o valor 8
  Entao a estrutura nao esta vazia
  E o elemento no final da estrutura tem o valor 8

    # Cenario 6
Cenario: Inserir mais de um valor no início do Deque.
  Dado que eu tenho um deque
  Quando insiro, no início da estrutura, os valores [4, 3, 2, 1]
  Entao a estrutura nao esta vazia
  E o elemento na frente da estrutura tem o valor 1
  E o elemento no final da estrutura tem o valor 4

    # Cenario 7
Cenario: Inserir um valor  no Deque, com elementos.
    Dado que eu tenho um deque
    E este deque tem os elementos, inseridos no final, [1, 3, 5, 7]
    Quando insiro, no início da estrutura, o valor 9
    Entao a estrutura nao esta vazia
    E o elemento na frente da estrutura tem o valor 9
    E o elemento no final da estrutura tem o valor 7


        # Cenario 8
Cenario: Remover um valor do final Deque.
  Dado que eu tenho um deque
  E este deque tem os elementos, inseridos no final, [1, 3, 5, 7]
  Quando eu retiro um elemento do final da estrutura
  Entao o elemento retirado tem o valor 7
  E o elemento na frente da estrutura tem o valor 1
  E o elemento no final da estrutura tem o valor 5

        # Cenario 9
Cenario: Remover um valor do inicio Deque.
  Dado que eu tenho um deque
  E este deque tem os elementos, inseridos no final, [1, 3, 5, 7]
  Quando eu retiro um elemento do inicio da estrutura
  Entao o elemento retirado tem o valor 1
  E o elemento na frente da estrutura tem o valor 3
  E o elemento no final da estrutura tem o valor 7

        # Cenario 10
Cenario: Remover um valor do inicio Deque.
  Dado que eu tenho um deque
  E este deque tem os elementos, inseridos no início, [1, 3, 5, 7]
  Quando eu retiro um elemento do inicio da estrutura
  Entao o elemento retirado tem o valor 7
  E o elemento na frente da estrutura tem o valor 5
  E o elemento no final da estrutura tem o valor 1

    # Cenario 11
Cenario: Remover um valor do final Deque.
  Dado que eu tenho um deque
  E este deque tem os elementos, inseridos no início, [1, 3, 5, 7]
  Quando eu retiro um elemento do final da estrutura
  Entao o elemento retirado tem o valor 1
  E o elemento na frente da estrutura tem o valor 7
  E o elemento no final da estrutura tem o valor 3

        # Cenario 11
Cenario: Remover um valor do final Deque.
  Dado que eu tenho um deque
  E este deque tem os elementos, inseridos no início, [1]
  Quando eu retiro um elemento do final da estrutura
  Entao o elemento retirado tem o valor 1
  E a estrutura esta vazia

        # Cenario 12
Cenario: Remover um valor do final Deque.
  Dado que eu tenho um deque
  E este deque tem os elementos, inseridos no final, [1]
  Quando eu retiro um elemento do inicio da estrutura
  Entao o elemento retirado tem o valor 1
  E a estrutura esta vazia
