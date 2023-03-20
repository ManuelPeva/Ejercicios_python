edad = int(input("Digite su edad: "))

'''forma sinplificada
if 0>edad<100:
'''

if edad>0 and edad<=100:
    print("Tu edad es correcta")
    if edad >=18:
        print("Es mayor de edad")
else:
    print("Edad incorrecta")