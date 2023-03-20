'''Escriba un programa que pida el peso (en kilogramos) y la altura (en metros)
    de una persona y que calcule su índice de masa corporal (imc)'''
import math

peso = float(input("Digite su peso: "))
altura = float(input("Digite su altura: "))

imc = peso / math.pow(altura,2)

print(f"Su imc es de: {imc:.1f}")