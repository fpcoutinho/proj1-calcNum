import numpy as np
import matplotlib.pyplot as pp
import math
import pandas as pd

# distancia da bola para a barreira no tiro livre = 9.14m
# altura do pulo médio dos jogadores mais altura média deles = 2.5m
# se até 9.14m a altura não for maior que 2.5, a bola vai bater na barreira

def calculaChute(velocidade, distancia):
    g = 9.8
    v0 = velocidade / 3.6
    seno = g * distancia / (v0 ** 2)

    try:
        if (seno > 1 or seno < -1):
            raise ValueError
    except ValueError:
        print("Cobrança pra fora!")
        return

    angRad = math.asin(seno) / 2
    angGraus = math.degrees(angRad)

    hMax = round((v0 ** 2) * (np.sin(angRad)) ** 2 / (2 * g), 1)
    tempoTotal = round((((2 * v0) * np.sin(angRad)) / g), 1)
    # alturaBarreira = 2.5
    # alturaTrave = 2.44
    # diametroBola = 0.22
    # centroBola = diametroBola / 2
    # melhorPosicaoSobTravePraChute = alturaTrave - centroBola
    tol = 1e-3
    muvD = lambda tn: distancia + (velocidade * np.sin(angGraus)) * tn + (g * tn ** 2) / 2
    muvV = lambda tn: (velocidade * np.sin(angGraus)) + g * tn
    ## metodo de newton
    tq0 = tempoTotal/2

    while True:
        iterator = 0
        tq1 = tq0 - (muvD(tq0) / muvV(tq0))

        print("tq1 =", abs(tq1))
        if tq1 - tq0 <= tol:
            break
        tq0 = tq1
        print("iteracao", iterator)
        iterator + 1

    # tempo da bola até chegar na altura necessaria para ficar fora do alcance do goleiro
    t2 = 2.15 / (np.sin(angRad) * v0)

    t = np.arange(0, tempoTotal - t2, 0.1)

    x = abs(v0) * np.cos(angRad) * t + (np.cos(angRad) * v0 * t2)
    y = (abs(v0) * np.sin(angRad) * t) - ((g * (t ** 2)) / 2)

    print("\n\n\n***")
    print("Ângulo do chute:", angGraus, "graus")
    print("Altura máxima:", hMax, "metros")
    print("Duração do lançamento:", tempoTotal, "segundos")
    print("***")

    pp.figure()
    pp.grid()
    pp.title("Trajetória do Projétil")
    pp.xlabel("Distância (m)")
    pp.ylabel("Altura (m)")
    pp.annotate("Barreira [2,5m]", xy=(9.14, 2.5), xycoords='data', xytext=(9, 2.55), textcoords='data')
    pp.bar(9.14, 2.5)
    pp.annotate("Gol [2,44m]", xy=(distancia, 2.44), xycoords='data', xytext=(distancia, 2.50), textcoords='data')
    pp.bar(distancia, 2.44)
    pp.plot(x, y)
    pp.show()


def main():
    while True:
        try:
            distancia = float(input("Digite a distância da cobrança para o gol (em m):"))
            if distancia <= 16.5 or distancia >= 45:
                raise ValueError

            v0 = float(input("Digite a velocidade (em km/h):"))
            if v0 <= 0:
                raise ValueError

            break
        except ValueError:
            print("Valor inválido! Favor informar somente valores positivos"
                  " para a velocidade e distância entre 16.5 e 45 metros.")
    calculaChute(v0, distancia)


if __name__ == "__main__":
    main()
