import numpy as np
import matplotlib.pyplot as pp
import math
import pandas as pd

# distancia da bola para a barreira no tiro livre = 9.14m
# altura do pulo médio dos jogadores mais altura média deles = 2.5m
# se até 9.14m a altura não for maior que 2.5, a bola vai bater na barreira


while True:
    try:
        distancia = float(input("Digite a distância da cobrança para o gol (em m):"))
        if distancia <= 16.5:
            raise ValueError

        v0 = float(input("Digite a velocidade (em km/h):"))
        if v0 <= 0:
            raise ValueError

        break
    except ValueError:
        print("Valor inválido! Favor informar somente valores positivos para a velocidade e ângulos entre 0 e 90 graus")

g = 9.8
v0 = v0/3.6
angRad = math.asin((g*distancia/(v0**2)))/2
angGraus = math.degrees(angRad)

hMax = round((v0 **2) * (np.sin(angRad)) **2 / (2 * g), 1)
tempoTotal = round((((2 * v0) * np.sin(angRad)) / g), 1)



t = np.arange(0, tempoTotal, 0.1)

x = abs(v0) * np.cos(angRad) * t
y = (abs(v0) * np.sin(angRad) * t) - ((g * (t ** 2)) / 2)

print("\n\n\n***")
print("Ângulo do chute:", angGraus, "graus")
print("Altura máxima:", hMax, "metros")
print("Duração do lançamento:", tempoTotal, "segundos")
print("***")

pp.title("Trajetória do Projétil")
pp.xlabel("Distância (m)")
pp.ylabel("Altura (m)")
pp.annotate("Barreira",
            xy=(9.14, 2.5),
            xycoords='data',
            xytext=(9, 2.55),
            textcoords='data')
pp.bar(9.14, 2.5)
pp.plot(x, y)
pp.show()