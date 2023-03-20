from turtle import *

"""
Encerramos el comportamiento en una función. 
"""


def cuadrado(longitud):
    # Cuatro veces...
    for i in range(4):
        # Ir hacia adelante
        forward(longitud)
        # Y girar 90 grados
        right(90)


# Yo no quiero animaciones
speed(0)
# Dibujar un cuadrado de 100
cuadrado(100)
# El input es para pausar el programa
input("Presiona Enter para salir...")