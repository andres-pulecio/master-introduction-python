# Creates a tuple with the months of the travel year. After this it requests numbers from the passenger, if the number is between 1 and the maximum length of the tuple, the program should display the contents of that position, otherwise it will display an error message.The program will terminate if the passenger enters a zero.
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

while True:
    num = int(input("Introduce un número entre 1 y {} (o 0 para salir): ".format(len(meses))))
    if num == 0:
        break
    elif 1 <= num <= len(meses):
        print(meses[num-1])
    else:
        print("Error: número fuera de rango")
