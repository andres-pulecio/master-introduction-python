# We need to know the letters in a ship's security code. The letters are repeated and it is very slow to know how many there are if we do it by hand. It is necessary to be able to enter the password for the supply store. We need to write a program that displays on the screen one by one the letters of the following code starting with the last one.
codigo = "saekrgvbnio"

for i in range(len(codigo)-1, -1, -1):
    print(codigo[i])
