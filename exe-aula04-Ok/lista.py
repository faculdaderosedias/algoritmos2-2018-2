#Leia dez números inseridos pelo usuário e responda:
#- Qual o maior número e qual o seu índice? TODO
#- Qual o menor número e qual o seu índice?
#- Qual a soma dos números pares?
#- Qual a soma dos números ímpares?
#- Qual a soma da divisão dos números de índice par, pelos números de índice ímpar?
#- Imprima os números na ordem inversa em que foram digitados.
#EXTRA: Leia um número arbitrário de números digitados pelo usuário,
#pare a entrada de dados quando o usuário entrar com o número zero (0).
from random import randint

lista = []
continuar = True
while continuar == True:
    numero = int(input("Digite um número:"))
    lista.append(numero)
    if numero == 0:
        continuar = False
    else:
        continuar = True

# lista = [randint(0, 100) for cont in range(10)]
# for contador in range(10):
#     numero = int(input("Digite um número:"))
#     lista.append(numero)

for numero in lista:
    print(numero)

# verificação menor
indice_menor  = 0
numero_menor = 0
for indice, numero in enumerate(lista):
    if indice == 0:
        indice_menor = indice
        numero_menor = numero
    elif numero < numero_menor:
        indice_menor = indice
        numero_menor = numero
print(f"Menor: Lista[{indice_menor}]={numero_menor}")

soma_pares = 0
soma_impares = 0
# soma dos números pares
for numero in lista:
    if numero % 2 == 0:
        soma_pares += numero # soma_pares = soma_pares + numero
    if numero % 2 != 0:
        soma_impares += numero # soma_pares = soma_pares + numero

print(f"Soma de pares: {soma_pares}")
print(f"Soma de ímpares: {soma_impares}")

soma_pares = 0
soma_impares = 0
for indice, numero in enumerate(lista):
    if indice % 2 == 0:
        soma_pares += numero
    if indice % 2 != 0:
        soma_impares += numero
calculo = soma_pares / soma_impares

print(f"Calculo {soma_pares} / {soma_impares} = {calculo}")
