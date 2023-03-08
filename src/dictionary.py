# We are going to create a program where we are going to declare a dictionary to store the prices of the different fruits that have been bought for the ship. The program will ask for the name of the fruit and the quantity that has been sold and will show us the final price of the fruit from the data stored in the dictionary. If the fruit does not exist it will give us an error. After each query the program will ask us if we want to make another query.
# Definimos el diccionario con los precios de las frutas
precios_frutas = {"manzana": 0.5, "pera": 0.4, "platano": 0.6, "naranja": 0.3}

# Pedimos al usuario que introduzca los datos de la fruta
while True:
    fruta = input("Introduce el nombre de la fruta: ")
    if fruta not in precios_frutas:
        print("Error: fruta no encontrada.")
        continue
    cantidad = float(input("Introduce la cantidad vendida en kilos: "))
    
    # Calculamos el precio total de la fruta
    precio_total = cantidad * precios_frutas[fruta]
    
    # Mostramos el precio total de la fruta
    print("El precio total de {} es de {} euros.".format(fruta, precio_total))
    
    # Preguntamos si se quiere hacer otra consulta
    opcion = input("¿Quieres consultar el precio de otra fruta? (S/N)").upper()
    if opcion != "S":
        break
