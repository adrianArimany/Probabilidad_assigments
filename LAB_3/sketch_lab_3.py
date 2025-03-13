from math import comb
import matplotlib.pyplot as plt

# Una caja contiene 5 pelotas blancas y 3 rojas. Suponga que se extraen 2 pelotas al azar sin reemplazo y $X$ denota el número de pelotas blancas. 

R = 3
W = 5
n = 2
 
# a. Determine $p(x)$ la función de masa de probabilidad de $X$.



# Probability mass function for X

# Notice is the Hypergeometric Distribution
# X ~ Hypergeometric(W, R, n) where W is the number of white balls, R is the number of red balls and n is the number of trials
# The probability mass function is given by:
# p(x) = C(W, x) * C(R, n-x) / C(W+R, n)
# where C(n, k) is the number of ways to choose k elements from a set of n elements
# In this case, the number of ways to choose x white balls from W white balls is C(W, x)
# The number of ways to choose n-x red balls from R red balls is C(R, n-x)
# The number of ways to choose n balls from W+R balls is C(W+R, n)
def pmf_x(x, R, W, n):
    return comb(W, x) * comb(R, n-x) / comb(W+R, n)

# Calculate probabilities
probabilities = {x: pmf_x(x, R, W, n) for x in range(0, n+1)}
print(probabilities)



# b. Determine $F(x)$ la función de distribución acumulada de $X$.

cumulative_probabilities = {x: sum([probabilities[i] for i in range(x+1)]) for x in range(n+1)}
print(cumulative_probabilities)

# c. Trace las representaciones gráficas de $p(x)$ y $F(x)$.

# plt.bar(probabilities.keys(), probabilities.values(), color='skyblue', alpha=0.7)
# plt.xlabel('Number of Observed White balls (X)')
# plt.ylabel('Probability')
# plt.title('Probability Mass Function (PMF) of X')
# plt.xticks(range(n+1))
# plt.show()

# plt.step(cumulative_probabilities.keys(), cumulative_probabilities.values(), where='mid', color='blue')
# plt.xlabel('Number of Observed White balls (X)')
# plt.ylabel('Accomulated Probabilities')
# plt.title('Accoumlated Probability Function (CDF) of X')
# plt.xticks(range(n+1))
# plt.ylim(0, 1.1)
# plt.show()

# d. Encuentre $E[x]$ y $Var(x)$.

expected_value = sum([x * probabilities[x] for x in probabilities])
print(f"E[X] = {expected_value:.4f}")

variance = sum([((x - expected_value)**2) * probabilities[x] for x in probabilities])
print(f"V[x] = {variance:.4f}")

#Repita el Ejercicio 1 suponiendo que las pelotas se extraen con reemplazo.

# Probability mass function for X

# Notice is the Binomial Distribution
# X ~ Bin(n, p) where n is the number of trials and p is the probability of success
# In this case, the probability of success is the probability of extracting a white ball
# The probability of extracting a white ball is W / (W + R)
# The probability of extracting a red ball is R / (W + R)
def pmf_x_replacement(x, R, W, n):
    return comb(n, x) * (W / (W + R)) ** x * (R / (W + R)) ** (n - x)



probabilities_with_replacement = {x: pmf_x_replacement(x, R, W, n) for x in range(0, n+1)}
print(probabilities_with_replacement)

# Accomulated Probability Function for X
cumulative_probabilities_replacement = {x: sum([probabilities_with_replacement[i] for i in range(x+1)]) for x in range(n+1)}
print(cumulative_probabilities_replacement)

# Graph PMF and CDF

# plt.bar(probabilities_with_replacement.keys(), probabilities_with_replacement.values(), color='skyblue', alpha=0.7)
# plt.xlabel('Number of Observed White balls (X)')
# plt.ylabel('Probability')
# plt.title('Probability Mass Function (PMF) of X')
# plt.xticks(range(n+1))
# plt.show()

# plt.step(cumulative_probabilities_replacement.keys(), cumulative_probabilities_replacement.values(), where='mid', color='blue')
# plt.xlabel('Number of Observed White balls (X)')
# plt.ylabel('Accomulated Probabilities')
# plt.title('Accoumlated Probability Function (CDF) of X')
# plt.xticks(range(n+1))
# plt.ylim(0, 1.1)
# plt.show()


# Calculate E[X] and Var(X)

expected_value_replacement = sum([x * probabilities_with_replacement[x] for x in probabilities_with_replacement])
print(f"E[X] = {expected_value_replacement:.4f}")

variance_replacement = sum([((x - expected_value)**2) * probabilities_with_replacement[x] for x in probabilities_with_replacement])
print(f"V[x] = {variance_replacement:.4f}")


# Sea $X$ una variable aleatoria que da el número de ases en una extracción al azar de 4 cartas de una baraja ordinaria de 52 cartas.

n = 4 # 4 cartas
k = 4 # 4 ases
R = 52 - 4 # 48 cartas no ases
W = 44  # 4 ases y 48 cartas no ases


# a. Determine $p(x)$ la función de masa de probabilidad de $X$.

probabilities_ases = {x: pmf_x(x, R, W, n) for x in range(0, n+1)}
print(probabilities_ases)

# b. Determine $F(x)$ la función de distribución acumulada de $X$.

cumulative_probabilities_ases = {x: sum([probabilities_ases[i] for i in range(x+1)]) for x in range(n+1)}
print(cumulative_probabilities_ases)


# c. Trace las representaciones gráficas de $p(x)$ y $F(x)$.

plt.bar(probabilities_ases.keys(), probabilities_ases.values(), color='skyblue', alpha=0.7)
plt.xlabel('Number of Observed White balls (X)')
plt.ylabel('Probability')
plt.title('Probability Mass Function (PMF) of X')
plt.xticks(range(n+1))
plt.show()

plt.step(cumulative_probabilities_ases.keys(), cumulative_probabilities_ases.values(), where='mid', color='blue')
plt.xlabel('Number of Observed White balls (X)')
plt.ylabel('Accomulated Probabilities')
plt.title('Accoumlated Probability Function (CDF) of X')
plt.xticks(range(n+1))
plt.ylim(0, 1.1)
plt.show()

# d. Encuentre $E[X]$ y $Var(X)$.

expected_value_ases = sum([x * probabilities_ases[x] for x in probabilities_ases])
print(f"E[X] = {expected_value_ases:.4f}")

variance_ases = sum([((x - expected_value_ases)**2) * probabilities_ases[x] for x in probabilities_ases])
print(f"V[x] = {variance_ases:.4f}")


# d. Calcule las probabilidades de $P(\{X\geq 2\})$ y $P(\{1\leq X\leq 3\})$.

probabilities_ases_ge_2 = sum([probabilities_ases[i] for i in range(2, n+1)])
print(f"P(X >= 2) = {probabilities_ases_ge_2:.4f}")

probabilities_ases_le_3 = sum([probabilities_ases[i] for i in range(1, 4)])
print(f"P(1 <= X <= 3) = {probabilities_ases_le_3:.4f}")