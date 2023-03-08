# We want to store the names and ages of the ship's passengers. Make a program that enters the name and age of each passenger. The data reading process will end when an asterisk * is entered as name.

# At the end the following data will be displayed:

# All passengers over the age of majority.
# Older passengers (those who are older
# Creamos una lista vacía para almacenar los pasajeros
pasajeros = []

# Pedimos el nombre y la edad de cada pasajero
while True:
    nombre = input("Introduce el nombre del pasajero (* para salir): ")
    if nombre == "*":
        break
    edad = int(input("Introduce la edad del pasajero: "))
    pasajeros.append((nombre, edad))  # Añadimos el pasajero a la lista como una tupla (nombre, edad)

# Mostramos todos los pasajeros mayores de edad
print("Pasajeros mayores de edad:")
for pasajero in pasajeros:
    if pasajero[1] >= 18:  # Comprobamos si la edad del pasajero es mayor o igual a 18
        print(pasajero[0])

# Buscamos el pasajero con mayor edad
mayor_edad = max(pasajeros, key=lambda x: x[1])  # La función max devuelve el elemento con mayor valor según la función lambda
print(f"El pasajero más mayor es {mayor_edad[0]} con {mayor_edad[1]} años.")
