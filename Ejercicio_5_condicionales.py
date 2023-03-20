'''Hacer un programa que simule un cajero automatico con un saldo inicial de
    $1000 y tendrá el siguiente menú de opciones:
       1.- Ingresar dinero en la cuenta\n"
      "2.- Retirar dinero de la cuenta\n"
      "3.- Mostrar dinero dispoible\n"
      "4.- Salir'''

saldo = 1000

print("1.- Ingresar dinero en la cuenta\n"
      "2.- Retirar dinero de la cuenta\n"
      "3.- Mostrar dinero dispoible\n"
      "4.- Salir")

opcion = int(input("\nDigite una opción del mundo: "))

if opcion == 1:
      mas = float(input("Cuanto dinero desea ingresar? "))
      saldo +=mas
      print(f"Tu dinero actual es de ${saldo}")
elif opcion==2:
      resta = float(input("Cuanto desea retirar: "))
      if resta>saldo:
            print("Notienes saldo suficiente")
      else:
            saldo -=resta
            print(f"Su saldo actual es de ${saldo}")
elif opcion==3:
      print(f"Dinero en la cuenta: {saldo}")
elif opcion==4:
      print("Gracias por usar ATM python")
else:
      print("error de solicitud")