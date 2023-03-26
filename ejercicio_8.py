'''Escriba un programa que pida una cantidad de segundos y que escriba cuántos minutos y segundos son.'''


segundos =  float(input("Digite la cantidad de segundos: "))

minutos = segundos/60

print(f"{segundos} segundos son {minutos:2f} minutos")