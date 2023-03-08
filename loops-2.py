# Write a program that stores the password string in a variable, ask the crew member for the password until the correct password is entered.
contraseña = "secreta123"  # definimos la contraseña

while True:  # repetimos hasta que la contraseña sea correcta
    intento = input("Introduce la contraseña: ")
    if intento == contraseña:
        print("Contraseña correcta")
        break  # salimos del bucle
    else:
        print("Contraseña incorrecta, inténtalo de nuevo")
