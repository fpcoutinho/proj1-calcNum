import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import math

def MetodoNewton(x,y,xi):
  #lendo tamanho de x para criação da matriz
  n = len(x)
  #criação da matriz(Tabela de diferenças divididas)
  matriz = [[None for x in range(n)] for x in range(n)]

  for i in range(n):
    matriz[i][0] = y[i]

  #Implementação da formula de diferença dividida para ser adicionanada na matriz
  for j in range(1,n):
    for i in range(n-j):
      matriz[i][j] = (matriz[i+1][j-1] - matriz[i][j-1])/(x[i+j]-x[i])

  #interpolação em xi a partir do metodo de Newton
  xterm = 1
  #Variável acumuladora:
  yp  = matriz[0][0]
  for ordem in range(1,n):
    xterm = xterm*(xi - x[ordem-1])
    yp  = yp + matriz[0][ordem]*xterm
  
  return yp

def calculaChute(velocidade, distancia):
    g = 9.8
    v0 = velocidade/3.6
    seno = g*(distancia)/(v0**2)

    try:
        if(seno>1 or seno <0):
            raise ValueError
    except ValueError:
        print("Cobrança pra fora!")
        return

    angRad = math.asin(seno)/2

    #tempo da bola até chegar na altura necessaria para ficar fora do alcance do goleiro.
    t2 = 2.1/(np.sin(angRad)*v0)
    #renovação das variaveis a partir da mudança de distância, devido a altura necessaria de chegada no gol.
    seno = g*(distancia+(np.cos(angRad)*v0*t2))/(v0**2)

    try:
        if(seno>1 or seno <0):
            raise ValueError
    except ValueError:
        print("Cobrança pra fora!")
        return

    
    angRad = math.asin(seno)/2
    angGraus = math.degrees(angRad)
    hMax = round((v0 **2) * (np.sin(angRad)) **2 / (2 * g), 1)
    tempoTotal = round((((2 * v0) * np.sin(angRad)) / g), 1)
    

    #tempo da bola até chegar na altura necessaria para ficar fora do alcance do goleiro
    
    t = np.arange(0, tempoTotal, 0.051)

    x = abs(v0) * np.cos(angRad) * (t)
    y = (abs(v0) * np.sin(angRad) * t) - ((g * (t ** 2)) / 2)

    print("\n\n\n***")
    print("Ângulo do chute:", angGraus, "graus")
    print("Altura máxima:", hMax, "metros")
    print("Duração do lançamento:", tempoTotal, "segundos")
    print("***")

    plt.figure()
    plt.grid()
    plt.title("Trajetória da Bola")
    plt.xlabel("Distância (m)")
    plt.ylabel("Altura (m)")
    plt.annotate("Barreira [2,5m]", xy=(9.14, 2.5), xycoords='data', xytext=(9, 2.55), textcoords='data')
    plt.bar(9.14, 2.5)
    plt.annotate("Gol [2,44m]", xy=(distancia, 2.44), xycoords='data', xytext=(distancia, 2.50), textcoords='data')
    plt.bar(distancia, 2.44)
    plt.bar(distancia, 2.1)
    plt.plot(x, y, 'r')
    
    #Variáveis para interpolação
    xBarreira = 9.14
    yBarreira = 2.7
    hGol = 2.15
    xhMax = (tempoTotal*np.cos(angRad)*v0)/2

    x1  = [0.0,xBarreira,xhMax, distancia]
    y1  = [0.0,yBarreira,hMax,hGol]
    xp = 0.5
    yp = MetodoNewton(x1,y1,xp) 
    t1  = np.arange(0, distancia, 0.1)
    yt = []
    for i in t1:
      yt.append(MetodoNewton(x1,y1,i))
    plt.plot(t1,yt,'b-')
    plt.plot(x1,y1,'o')
    plt.plot(xp,yp,'-g')
    plt.grid()
    plt.show()
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
