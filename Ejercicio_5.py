'''Una tienda ofrece un descuento del 15% sobre el total de la compra y
    un cliente desea saber cuánto deberá pagar finalmente por su compra'''

precio = float(input("Digite el precio del producto: "))

des = precio * 0.15

precio_final = precio - des

print(f"El precio final es ${precio_final:.2f}")

'''opción 2
precio = float(input("Digite el precio: "))
a = float(input("Digite el descuento: "))

a /=100

descuento = precio * a

precio_final = precio - descuento

print(precio_final)
'''