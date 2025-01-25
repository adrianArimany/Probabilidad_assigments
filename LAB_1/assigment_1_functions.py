# Problema A1
import itertools as it
print("Problema A1:")
S = {"A", "B", "C", "D", "E", "F", "G", "H"}

# Para simplificar, tomemos solo la primera letra de los nombres.
re1 = set(it.combinations(S, 3))
result = len(re1)

getA = 0
for i in re1:
     if "A" in i:
          getA += 1
         
         
print(result)
print(getA)
# Resultado: 56, 21

# Problema B1
print("Problema B1:")



#Resultado: 70,35