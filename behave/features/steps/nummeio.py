from behave import given, when, then
from sistema import nummeio

@given(u' uma lista de numeros ({num1}, {num2}, {num3})')
def given_umalista(context, num1, num2, num3):
      """Define numeros dados a lista."""
    context.num = (string(num1), string(num2), string(num3)),


@when(u'verificar qual o num do meio')
def when_verificonummeio(context):
    num1 = context.num1
    num2 = context.num2
    num3 = context.num3
    context.meio = mum_meio(num1, num2, num3)


@then(u'o resultado esperado e {num2}')
def then_impl(context, esperado):
    """Testa se o num do meio esta correto"""
    expected = True if esperado == "num2" else False
    assert context.meio == nummeio
