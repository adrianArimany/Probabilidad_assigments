import itertools as it
import matplotlib.pyplot as plt
import numpy as np

#En una caja con 20 pelotas numeradas del 1 al 20, se seleccionan cuatro pelotas al azar. Sea $X$ el número más grande de pelota seleccionada una variable aleatoria.

#- la función de masa de probabilidad de $X$
#- la función de densidad acumulada de probabilidad de $X$

A = set(range(1,21))
S = set(it.product(A,repeat=4))

R = [(m,len([k for k in S if max(k) == m])) for m in range(1,21)]
X = [k[0] for k in R] # Variable aleatoria
P = [round(k[1]/len(S),3) for k in R] # Medida de probabilidad de cada evento

# Gráfico de barras
plt.bar(X, P, tick_label=[str(k) for k in X])
plt.xlabel("Resultado del lanzamiento")
plt.ylabel("Probabilidad")
plt.title("Función de Masa de Probabilidad (PMF)")
plt.ylim(0, max(P)+0.1)
    
# Mostrar valores en las barras
for i, prob in zip(X, P):
    plt.text(i, prob + 0.05, str(prob), ha='center', fontsize=10)
    
plt.show()

# Gráfico de escalón
acum = 0
for i in range(len(X)-1):
    acum += P[i]
    plt.step([X[i],X[i+1]],[acum, acum],where='pre',color='blue')
plt.step([X[-1], X[-1]+1], [sum(P), sum(P)], where='pre',color='blue')

plt.xlabel("Resultado del lanzamiento")
plt.ylabel("Probabilidad acumulada")
plt.title("Función de Distribución Acumulada (CDF)")
plt.xticks(X, [str(k) for k in X])
#plt.yticks(np.linspace(0,1,int(1/P[0])+1))
plt.show()