# The ship's passengers have been divided into two groups A and B according to gender and name. Group A consists of women with a name before M and men with a name after N and group B consists of the rest. Write a program that asks the passenger his name and sex, and displays on the screen the group that corresponds to him.
# Pedir al usuario su nombre y sexo
nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (M/F): ")

# Determinar el grupo correspondiente
if (sexo == "F" and nombre.lower() < "M") or (sexo == "M" and nombre.lower() > "N"):
    grupo = "A"
else:
    grupo = "B"

# Mostrar el grupo correspondiente por pantalla
print("Tu grupo es", grupo)
