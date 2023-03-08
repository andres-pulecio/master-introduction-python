# Write a program that stores the password string in a variable, asks the user for the password and prints on the screen if the password entered by the user matches the password stored in the case insensitive variable.
# Almacenar la contraseña en una variable
contraseña = "MiContraseña123"

# Pedir al usuario que introduzca una contraseña
contraseña_usuario = input("Introduce la contraseña: ")

# Comprobar si la contraseña coincide sin tener en cuenta mayúsculas y minúsculas
if contraseña.lower() == contraseña_usuario.lower():
    print("¡Contraseña correcta!")
else:
    print("Contraseña incorrecta.")
