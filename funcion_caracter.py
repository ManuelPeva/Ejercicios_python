""" Escribir una función que tome un carácter y devuelva True si es
una vocal, de lo contrario devuelve False"""

def es_vocal(caracter):

    vocal = ["a","e","i","o","u"]
    
    if(caracter.lower() in vocal):
        return True
    else:
        return False
    


print(es_vocal("a"))
print(es_vocal("E"))
print(es_vocal("z"))


