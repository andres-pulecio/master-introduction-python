# On the ship, your crew members are evaluated weekly. The points they can get in the evaluation start at 0.0 and can increase, translating into better ranks. The points that crew members can get can be 0.0, 0.4, 0.6 or more, but not intermediate values between the mentioned figures. A table with the levels corresponding to each score is shown below. The total amount of points scored in each level is 2,400 multiplied by the level score.
puntuacion = float(input("Introduce la puntuación del tripulante: "))
if puntuacion == 0.0:
    nivel = "Inaceptable"
    puntos_totales = 0.0
elif puntuacion == 0.4:
    nivel = "Aceptable"
    puntos_totales = 2400 * puntuacion
else:
    nivel = "Meritorio"
    puntos_totales = 2400 * puntuacion
    
print("El nivel de rendimiento del tripulante es", nivel)
print("La puntuación total del tripulante es", puntos_totales)

