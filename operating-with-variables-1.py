# We need to know which door the food opens for the passengers and crew. To do this we need to write a program that reads a positive integer, n, entered by the crew member and then displays on the screen the sum of all the integers from 1 to n. The formula for this problem is: sum=n(n+1)2.
# Pedir al usuario que introduzca un entero positivo
n = int(input("Introduce un entero positivo: "))

# Calcular la suma de todos los enteros desde 1 hasta n
suma = n * (n + 1) / 2

# Mostrar la suma por pantalla
print("La suma de todos los enteros desde 1 hasta", n, "es:", int(suma))
