# Code a program that allows us to store the names of the crew members and the notes of the interstellar academy. Each crew member can have a different number of notes. Store the information in a dictionary whose keys will be the names of the crewmembers and the values will be listed with the notes of each crewmember.
 
# The program will ask for the number of crew members we are going to enter, it will ask for their names and will ask for their grades until we enter a negative number. At the end the program will show us the list of crew members and the average grade obtained by each of them.


# Note: if you enter the name of a crew member that already exists, the program will give us an error.
tripulantes = {}
n = int(input("Introduce el número de tripulantes: "))

for i in range(n):
    nombre = input(f"Introduce el nombre del tripulante {i+1}: ")
    
    if nombre in tripulantes:
        print("Error: ese tripulante ya existe en la lista")
        continue
    
    notas = []
    nota = float(input("Introduce una nota (introduce un número negativo para terminar): "))
    while nota >= 0:
        notas.append(nota)
        nota = float(input("Introduce otra nota (introduce un número negativo para terminar): "))
    
    tripulantes[nombre] = notas

for nombre, notas in tripulantes.items():
    media = sum(notas) / len(notas)
    print(f"{nombre}: {notas} - Nota media: {media:.2f}")
