'''Hacer un programa que pida 3 numeros y determine cuál es el mayor'''

num1 = int(input("Digite el numero: "))
num2 = int(input("Digite el numero: "))
num3 = int(input("Digite el numero: "))

if num1==num2 and num2==num3 and num1==num3:
    print("Todos son iguales")
elif num1>num2 and num1>num3:
    print(f"{num1} es mayor")
elif num2>num1 and num2>num3:
    print(f"{num2} es mayor")
elif num3>num2 and num3>num2:
    print(f"{num3} es mayor")