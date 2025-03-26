'''
Determina el mayor de tres numeros ingresando
por el teclado
'''

numeros = []
for i in range(1, 4):
    numero = int(input(f"Ingrese el número {i}: "))
    numeros.append(numero)

mayor = sorted(numeros, reverse=True)[0]

print(f"El número mayor entre {numeros[0]}, {numeros[1]} y {numeros[2]} es: {mayor}")