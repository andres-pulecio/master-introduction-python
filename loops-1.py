# In order to refuel we have to manage to write a Python program that asks the crew member for an integer number and displays a right triangle like the one below, with the height of the number entered:

# *

# **

# ***

# ****

# *****
n = int(input("Introduce un número entero: "))
for i in range(1, n+1):
    print("*" * i)

