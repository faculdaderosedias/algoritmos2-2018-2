#Criar uma função, utilizando a linguagem Python, para encontrar,
#entre três números, qual dos três fica entre os dois extremos.
#Crie cenários de teste utilizando a ferramento Behave.

def num_meio (num1, num2, num3):
    """Verificar maior três"""
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3
