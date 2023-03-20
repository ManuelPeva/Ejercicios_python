'''Hacer un programa para ingresar el radio de un circulo y se reporte
    su área y la longitud de la circunferencia'''
import math
import matplotlib.pyplot as plt
'''Trazar la figura'''
figure, axes = plt.subplots()
draw_circle = plt.Circle((0.5,0.5), 0.3)

axes.set_aspect(1)
axes.add_artist(draw_circle)
plt.title('Circulo')
plt.show()

''''''

r = float(input("Digite el valor del radio: "))

area = math.pi * math.pow(r,2)
longitud = 2 * math.pi * r

print(f"El area es de: {area:.2f} y la longitud es de: {longitud:.2f}")

