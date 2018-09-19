"""Funcao em Python que que verifica se um ponto está dentro de um retângulo.
Verificar se uma coordenada está dentro de um retângulo.
Considerando os pontos:
A(x7;y8)
B(x6;y7).

Cenario: Um ponto está dentro do retângulo.
    Dado um ponto com as coordenadas (7, 8)
    Dado um retângulo nas coordenadas (6,7) e dimensão (2,2)
    Quando quero saber se o ponto está dentro do retangulo
    Entao o resultado é verdadeiro.
"""
def calcula_coordenada():
    qtd_retangulo, qtd_pontos = raw_input().split()
    raios_retangulo = [float(raw_input()) for retangulo in range(int(qtd_pontos))]
    cord_tiros = [raw_input().split() for tiro in range(int(qtd_tiros))]
    pontos = 0
    for x, y in cord_tiros:
        for raio in raios_circulos:
            if((int(x) ** 2) + (int(y) ** 2) > (raio ** 2)):
                continue
            else:
                pontos += 1
    print pontos

calcula_pontos()
