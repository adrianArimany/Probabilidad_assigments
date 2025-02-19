#Supongamos que se lanza una moneda cuatro veces. Sea $X$ el número de caras en la secuencia observada una variable aleatoria.

#a. Elabore una tabla de frecuencias de los valores de $X$.

#b. Liste los resultados del evento $\{X=3\}$.

import itertools as it
import math


def coin(n):
    #Assuming each observed random vaariable is independent, by the multiplication rule we can form a product of independent random variables
    #Here we define p = 1 (as success or the observaed random variable is a head); q = 0 (failure or the observed random variable is a tail)
    return it.product([0, 1], repeat=n)

def freq_table(iterable):
    #Define the list
    freq = {}
    for x in iterable:
        heads_count = sum(x) #We sum all the observed heads in the 4-tuple of (0,1)
        freq[heads_count] = freq.get(heads_count, 0) + 1 #Counts the frequency that there is a success p in the tuple.
    return freq #returns the event {X=0:frequency, X=1: frequency,..., X=4: frequency}

if sum(freq_table(coin(4)).values()) == len(list(coin(4))): #We check if the sum of the 16 possible outcomes is equal to the number of possible outcomes
    print(f"There is a total of {len(list(coin(4)))} possible outcomes")
    print(f"The sum of the frequencies is {sum(freq_table(coin(4)).values())} and it is equal to the number of possible outcomes")
    print(f"The frequencies are: {freq_table(coin(4))}")
else:
    print("Error: The sum of the frequencies is not equal to the number of possible outcomes") 



def exact_event(n):
    outcomes = [x for x in coin(4) if sum(x) == n] #So the list is stored in a single line
    if outcomes:
        print(f"The number of events where (X={n}) is:", len(outcomes))
        print(f"The events where (X={n}) are:", outcomes)
    else:
        print(f"Notice: There are no events where (X={n})")
exact_event(3)


#Supongamos que se lanzan tres dados. Sean $X$ la suma de los dados y $Y$ el producto de los dados, variables aleatorias.

#a. Elabore una tabla de frecuencias de los valores de $X$. ¿Cuál es el más frecuente? ¿Cuántas veces ocurrió?

#b. Elabore una tabla de frecuencias de los valores de $Y$. ¿Cuál es el más frecuente? ¿Cuántas veces ocurrió?

#c. Liste los resultados del evento $\{X\leq 5\}$.

#d. Liste los resultados del evento $\{8\leq Y\leq 12\}$.

### a

def die_sumX(n):
    return (sum(x) for x in it.product(range(1, 7), repeat=n))

def freq_table_sumX(iterable):
    freq = {}
    for x in iterable:
        freq[x] = freq.get(x, 0) + 1
    return freq


def highest_frequencies(freq):
    highest_freq = max(freq.values())
    return [k for k,v in freq.items() if v == highest_freq]

def frequency_table_sumX_result(n):
    freq = freq_table_sumX(die_sumX(n))
    if sum(freq.values()) == len(list(die_sumX(n))):
        print(f"The sum of the frequencies is {sum(freq.values())} and it is equal to the number of possible outcomes")
        print(f"The frequencies are: {freq}")
        print("Also: ")
        highest_freqs = highest_frequencies(freq)
        if len(highest_freqs) > 1:
            print(f"There are {len(highest_freqs)} highest frequencies of {max(freq.values())} at X={', '.join(map(str, highest_freqs))}")
        else:
            print(f"The highest frequency is {max(freq.values())} at X={max(freq, key=freq.get)}")
    else:
        print("Error: The sum of the frequencies is not equal to the number of possible outcomes")

frequency_table_sumX_result(3)

### b
def die_productY(n):
    return (math.prod(x) for x in it.product(range(1, 7), repeat=n))

def freq_table_productY(iterable):
    freq = {}
    for y in iterable:
        freq[y] = freq.get(y, 0) + 1
    return freq

def frequency_table_productY_result(n):
    freq = freq_table_productY(die_productY(n))
    if sum(freq.values()) == len(list(die_productY(n))):
        print(f"The sum of the frequencies is {sum(freq.values())} and it is equal to the number of possible outcomes")
        print(f"The frequencies are: {freq}")
        print("Also: ")
        highest_freqs = highest_frequencies(freq)
        if len(highest_freqs) > 1:
            print(f"There are {len(highest_freqs)} highest frequencies of {max(freq.values())} at Y={', '.join(map(str, highest_freqs))}")
        else:
            print(f"The highest frequency is {max(freq.values())} at Y={max(freq, key=freq.get)}")
    else:
        print("Error: The sum of the frequencies is not equal to the number of possible outcomes")

frequency_table_productY_result(3)


#### c

def leq_sum(n, die_count):
    outcomes = [x for x in die_sumX(die_count) if x <= n]
    if outcomes:
        print(f"The number of events where (X<={n}) is:", len(outcomes))
        print(f"The events where (X<={n}) are:", outcomes)
    else:
        print(f"Notice: There are no events where (X<={n})")
leq_sum(n = 5, die_count=3)

#### d

def leq_product(n,m, die_count):
    outcomes = [y for y in die_productY(die_count) if n <= y <= m]
    if outcomes:
        print(f"The number of events where ({n}<=Y<={m}) is:", len(outcomes))
        print(f"The events where ({n}<=Y<={m}) are:", outcomes)
    else:
        print(f"Notice: There are no events where ({n}<=Y<={m})")
leq_product(n = 8, m = 12, die_count=3)

