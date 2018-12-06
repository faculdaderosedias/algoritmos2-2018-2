@"""Testes da Funcionalidade Calculo da media.


from behave import given, when, then

from sistema import media


@given('os numeros 2 e 4')
def given_dois_numero(context):
    context.num1 = 2
    context.num2 = 4
    """Dado que o sistema tenha dois  valores."""


@when('calculo a media de dois numeros')
def when_calcula_media(context):
    context.resultado = media(context.num1 + context.num2 )
    """Forcao co calculo da media"""



@then('o resultado e 3')
def then_verifica_media(context):
    assert context.resultado ==3
    """Verifica o calculo da media"
