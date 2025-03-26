'''
Determina el mayor de tres numeros ingresando
por el teclado
'''

def intercambiar_valores(numero1, numero2):
    temporal = numero1
    numero1 = numero2
    numero2 = temporal
    return numero1, numero2


numero1=int(input("Ingrese el primero numero: "))
numero2=int(input("Ingrese el segundo numero: "))
numero3=int(input("Ingrese el tercer numero: "))

if numero1>numero2:
    numero1, numero2 = intercambiar_valores(numero1, numero2)

if numero2>numero3:
    numero2, numero3 = intercambiar_valores(numero1, numero3)

if numero1>numero2:
    numero2, numero3 = intercambiar_valores(numero1, numero2)


print(f"numero ordenados: {numero1}, {numero2}, {numero3}")
print(f"El mayor es {numero3}")