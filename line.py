#11/4/2025
#TP4 - Rozas Miguel Agustin - Introduccion a la programacion 1
# Ejercicio 1
#
import math
def line():
    A = float(input("Ingrese el coeficiente A:")) 
    B = float(input("ingrese el coeficiente B:"))
    X1 = float(input("Ingrese el coeficiente X1:"))
    X2 = float(input("Ingrese el coeficiente X2:"))
    Y1 = A*X1 + B
    Y2 = A*X2 + B
    Cat1 = float(X2 - X1)
    Cat2 = float(Y2 - Y1)
    distance = float(math.sqrt(math.pow(Cat1,2) + math.pow(Cat2,2)))
    print(f"El coeficiente A de su ecuación de la recta es:", A)
    print(f"El coeficiente B de su ecuación de la recta es:", B)
    print(f"El coeficiente X1 de su ecuación de la recta es:", X1)
    print(f"El coeficiente X2 de su ecuación de la recta es:", X2)
    print("")
    print("Para la siguiente ecuación:")
    print(f"\tY = {A}X + {B}\n") #usar {} para eliminar espacios
    print("Dados los siguientes puntos:")
    print(f"\tP1 ({X1}, {Y1})")
    print(f"\tP2 ({X2}, {Y2})\n")
    print(f"La distancia entre ellos es: {distance}")
