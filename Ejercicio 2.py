'''Determinar la solución lógica de la siguiente operación'''

a = float(input("Digita el valor de a: "))
b = float(input("Digita el valor de b: "))

expresion = ((3+5*8)<3 and ((-6/3*4)+2<2)) or (a>b)
print(expresion)