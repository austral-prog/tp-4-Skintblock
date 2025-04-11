#11/4/2025
#TP4 - Rozas Miguel Agustin - Introduccion a la programacion 1
# Ejercicio 2
#
#
def leap_year():
    year = int(input("Ingrese un año: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
        print("El año", year, "es bisiesto")
    else:
        print("El año", year, "no es bisiesto") 
