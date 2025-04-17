''' Determina el mayor de tres numeros ingresando por el teclado '''
numeros = []
for i in range(1, 4):
    numero = int(input(f"Ingrese el número {i}: "))
    numeros.append(numero)

if numeros[0] >= numeros[1] and numeros[0] >= numeros[2]:
    mayor = numeros[0]
elif numeros[1] >= numeros[0] and numeros[1] >= numeros[2]:
    mayor = numeros[1]
else:
    mayor = numeros[2]

print(f"El número mayor entre {numeros[0]}, {numeros[1]} y {numeros[2]} es: {mayor}")
