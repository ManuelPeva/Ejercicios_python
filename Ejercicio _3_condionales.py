'''Hacer un programa que pida un crácter e indique si es una vocal o no'''
#upper() pasa todo pasa mayusculas
caracter = str(input("Digite un caracter: ").lower())
#manera simple
#if letra=='a' or letra=='b':
if caracter== 'a':
    print(f"{caracter} es una vocal")
elif caracter=='e':
    print(f"{caracter} es una vocal")
elif caracter=='i':
    print(f"{caracter} es una vocal")
elif caracter=='o':
    print(f"{caracter} es una vocal")
elif caracter=='u':
    print(f"{caracter} es una vocal")
else:
    print(f"{caracter} esto no es una vocal")
