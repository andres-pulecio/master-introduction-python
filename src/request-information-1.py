# Write a program that asks the crew member for the number of hours worked and the cost per hour. It should then display the crew member's pay on the screen.
# Pedir al usuario el número de horas trabajadas y el coste por hora
horas_trabajadas = float(input("Introduce el número de horas trabajadas: "))
coste_por_hora = float(input("Introduce el coste por hora: "))

# Calcular la paga correspondiente
paga = horas_trabajadas * coste_por_hora

# Mostrar la paga correspondiente por pantalla
print("La paga correspondiente es:", paga)
