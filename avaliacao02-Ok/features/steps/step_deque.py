"""Testes da Prova de Algoritmos 2."""

from behave import given, when, then

from deque import Deque


@given('o tamanho da estrutura sendo 10')
def _given_tamanho_estrutura(context):
    context.tamanho = 10


@when('crio um deque')
def _when_crio_deque(context):
    context.deque = Deque(context.tamanho)


@then('a estrutura esta vazia')
def _then_deque_vazia(context):
    assert context.deque.empty() is True


@then('tenho um deque com capacidade para armazenar 10 elementos')
def _then_deque_capacity(context):
    assert context.deque.capacity() == 10


# Cenario 2
@given('que eu tenho um deque')
def _given_deque_criado(context):
    context.deque = Deque(10)


@when('insiro, no final da estrutura, o valor {valor:d}')
def _when_insere_final(context, valor):
    context.deque.pushBack(valor)


@then('a estrutura nao esta vazia')
def _then_deque_nao_vazia(context):
    assert context.deque.empty() is False


@then('o elemento na frente da estrutura tem o valor {valor:d}')
def _then_elemento_na_frente(context, valor):
    expected = valor
    observed = context.deque.peekFront()
    print("E: {}, O:{}".format(expected, observed))
    assert expected == observed


# Cenario 3
@when('insiro, no final da estrutura, os valores [{lista}]')
def _when_insere_varios_elementos(context, lista):
    for elemento in lista.split(', '):
        context.deque.pushBack(int(elemento))


@then('o elemento no final da estrutura tem o valor {valor:d}')
def _then_elemento_no_final(context, valor):
    assert context.deque.peekBack() == valor


# Cenario 4
@given('este deque tem os elementos, inseridos no final, [{lista}]')
def _given_deque_com_elementos(context, lista):
    context.deque = Deque(10)
    for elemento in lista.split(', '):
        context.deque.pushBack(int(elemento))


# Cenario 5
@when('insiro, no início da estrutura, o valor {valor:d}')
def _when_inser_inicio(context, valor):
    context.deque.pushFront(valor)


# Cenario 6
@when('insiro, no início da estrutura, os valores [{lista}]')
def _when_insere_varios_elementos_inicio(context, lista):
    for elemento in lista.split(', '):
        context.deque.pushFront(int(elemento))


# Cenario 7
@given('este deque tem os elementos, inseridos no início, [{lista}]')
def _given_deque_com_elementos_no_inicio(context, lista):
    context.deque = Deque(10)
    for elemento in lista.split(', '):
        context.deque.pushFront(int(elemento))


# Questao 4
# Cenario 8
@when('eu retiro um elemento do final da estrutura')
def _when_remove_final(context):
    context.result = context.deque.popBack()


@then('o elemento retirado tem o valor {valor:d}')
def _then_elemento_retirado_tem_valor(context, valor):
    assert context.result == valor


# Cenario 9
@when('eu retiro um elemento do inicio da estrutura')
def _when_remove_final(context):
    context.result = context.deque.popFront()
