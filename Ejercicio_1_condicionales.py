'''Hacer un programa que pida al usuario dos numeros y se de cuenta cuál de
   ellos es par, o si ambos lo son'''

a = int(input("Digite un numero: "))
b = int(input("Digite otro numero: "))

if a%2==0 and b%2==0:
    print("Abos numeros son pares")
elif a%2==0 and b%2!=0:
    print(f"{a} es par")
elif a%2!=0 and b%2==0:
    print(f"{b} es par")
else:
    print("Ningun numero es par")