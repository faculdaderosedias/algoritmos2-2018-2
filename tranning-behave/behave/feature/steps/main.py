#Exemplo Professor
#"""Define uma classe Retangulo com tratamento de colisao."""

#class Retangulo:
#    """Define objetos do tipo retangulo."""

#    def __init__(self, x, y, w, h):
#        """Inicializa objeto retangulo."""
#        self.y = y
#        self.width = w
#        self.height = h

########STEP MAIN.PY#########
from behave import *

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False
