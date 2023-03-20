'''Construir un programa que simule el funcionamiento de una calculadora que puede realizar las cuatro operaciones aritmeticas basicas
    . el usuario debe especificar la operación con el primer caracter del nombre de la operación
'''

print("s == Suma\n"
      "r == Resta\n"
      "p, m == Multiplicación\n"
      "d == División")

var = input("\nDigite una letra dentro del menu: ".lower())

a = float(input("\nDigita el valor de a: "))
b = float(input("Digita el valor de b: "))

resultado = 0

if var == 's':
      resultado = a+b
      print(f"La suma es:igual a: {resultado}")
elif var == 'r':
      resultado = a-b
      print(f"La resta es igual a: {resultado}")
elif var == 'm' or var=='p':
      resultado = a*b
      print(f"La multiplicación es igual a: {resultado}")
elif var == 'd':
      resultado = a/b
      print(f"La división es igual a: {resultado}")
else:
      print("No esta en el menu")