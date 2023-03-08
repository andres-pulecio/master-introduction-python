# Pedir al usuario el número de horas trabajadas y el coste por hora
horas_trabajadas = float(input("Introduce el número de horas trabajadas: "))
coste_por_hora = float(input("Introduce el coste por hora: "))

# Calcular la paga correspondiente
paga = horas_trabajadas * coste_por_hora

# Mostrar la paga correspondiente por pantalla
print("La paga correspondiente es:", paga)
