# Dos números del 1 al 10 se seleccionan sucesivamente al azar. 

# ¿Cuál es la probabilidad de que su producto sea menor o igual que 50?
import itertools as it
x = range(1,11)
total_cases = len(list(it.product(x,x)))
favorable_cases = len([k for k in it.product(x,x) if k[0]*k[1] <= 50])
probability = favorable_cases / total_cases
print(probability)

#Si se lanza un dado 4 veces, ¿cuál es la probabilidad de que salga 6 al menos una vez?

x =range(1,7) #this is your die, with probabiliy 1/6
total_cases = len(list(it.product(x,x,x,x))) #we roll the dice 4 times 
favorable_cases = len([k for k in it.product(x,x,x,x) if k[0] == 6 or k[1] == 6 or k[2] == 6 or k[3] == 6]) #as long as one die rolls a 6, we take that result as success.
probability = favorable_cases / total_cases
print(probability)
# En un colegio, 3/4 de los estudiantes participan en deportes, 1/2 en actividades culturales y 1/8 en ninguna de ellas. Calcule la probabilidad de que un estudiante participe:
Deporte = 3/4
Culturales = 1/2
Complement_x_And_y = 1/8

#By Axiom 2, we know that the P(SampleSpace) = 1, 

# a) en deportes o en actividades culturales
X_OR_Y = 1 - Complement_x_And_y #= P(Deporte OR Culturales)
print(X_OR_Y)

# b) tanto deportes como actividades culturales
X_AND_Y = Deporte + Culturales - X_OR_Y #by properties of the axioms of probability
print(X_AND_Y)



# c) actividades culturales pero no deportivas
Y_MINUS_X = Culturales - X_AND_Y #by properties of the axioms of probability
print(Y_MINUS_X)


# Una urna contiene 5 pelotas rojas, 6 azules y 8 verdes. Si se selecciona al azar un conjunto de 3 pelotas, ¿cuál es la probabilidad de que cada una de las pelotas sea:
urn = {'Red': 5, 'Blue': 6, 'Green': 8}
x = urn['Red'] + urn['Blue'] + urn['Green']

# a) del mismo color?
total_ways = len(list(it.combinations(range(x), 3)))
total_ways_same_color = len(list(it.combinations(range(urn['Red']), 3))) + len(list(it.combinations(range(urn['Blue']), 3))) + len(list(it.combinations(range(urn['Green']), 3)))
probability_same_color = total_ways_same_color / total_ways
print(probability_same_color)

# b) de colores diferentes? 



##### DANIEL ...........
# Problema 4:
total_red = 5
total_blue = 6
total_green = 8

total_balls = total_red + total_blue + total_green

total_combinations = list(it.combinations(range(total_balls), 3))
total_count = len(total_combinations)


red_combinations = list(it.combinations(range(total_red), 3))
red_count = len(red_combinations)

blue_combinations = list(it.combinations(range(total_red, total_red + total_blue), 3))
blue_count = len(blue_combinations)


green_combinations = list(it.combinations(range(total_red + total_blue, total_balls), 3))
green_count = len(green_combinations)

same_color_count = red_count + blue_count + green_count
same_color_probability = same_color_count / total_count

different_color_count = total_red * total_blue * total_green
different_color_probability = different_color_count / total_count

print(f"Probabilidad de que las 3 pelotas sean del mismo color: {same_color_probability:.4f}")
print(f"Probabilidad de que las pelotas sean de colores diferentes: {different_color_probability:.4f}")

# Problema 5:
# Repita el ejercicio anterior suponiendo que ahora cada vez que se selecciona una pelota, 
# se anota su color y se vuelve a introducir en la urna antes de la siguiente selección; 
# esto se conoce como _muestreo con reemplazo._
total_red = 5
total_blue = 6
total_green = 8

total_balls = total_red + total_blue + total_green

p_red = total_red / total_balls
p_blue = total_blue / total_balls
p_green = total_green / total_balls

p_same_color = (p_red * 3) + (p_blue * 3) + (p_green ** 3)


p_different_colors = 6 * (p_red * p_blue * p_green)

print(f"Probabilidad de que las 3 pelotas sean del mismo color: {p_same_color:.4f}")
print(f"Probabilidad de que las pelotas sean de colores diferentes: {p_different_colors:.4f}")

##### Problema 6:
# Un profesor da a su clase un conjunto de 10 problemas con la información de que el examen final consistirá en una selección aleatoria de 5 de ellos. 
# Si un estudiante ha resuelto 7 de los problemas, 
# ¿cuál es la probabilidad de que conteste correctamente:

# a) los 5 problemas?

# b) al menos 4 de los problemas?

total_problems = 10  
solved_problems = 7  
exam_problems = 5   


total_combinations = len(list(it.combinations(range(total_problems), exam_problems)))


correct_5_combinations = len(list(it.combinations(range(solved_problems), exam_problems)))


probability_correct_5 = correct_5_combinations / total_combinations



correct_4_combinations = len(list(it.combinations(range(solved_problems), 4)))

incorrect_1_combinations = len(list(it.combinations(range(solved_problems, total_problems), 1)))


correct_4_total = correct_4_combinations * incorrect_1_combinations

at_least_4_combinations = correct_4_total + correct_5_combinations


probability_at_least_4 = at_least_4_combinations / total_combinations


print(f"Total de combinaciones posibles del examen: {total_combinations}")
print(f"Probabilidad de acertar los 5 problemas: {probability_correct_5:.4f}")
print(f"Probabilidad de acertar al menos 4 problemas: {probability_at_least_4:.4f}")