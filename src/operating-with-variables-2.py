# In order to know what protective suit we need in case of leaving the ship, it is necessary to know the body mass index. To know it we are going to write a program that asks the crew member for his weight (in kg) and height (in meters), calculates the body mass index and stores it in a variable, and displays the sentence "Your body mass index is <imc>" where <imc> is the calculated body mass index rounded to two decimal places.
# Pedir al usuario su peso y estatura
peso = float(input("Introduce tu peso en kg: "))
estatura = float(input("Introduce tu estatura en metros: "))

# Calcular el índice de masa corporal
imc = peso / (estatura ** 2)

# Mostrar el índice de masa corporal por pantalla
print("Tu índice de masa corporal es", round(imc, 2))
