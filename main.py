''' Determina el mayor de tres números ingresados por teclado con validación '''

def pedir_numero(indice):
    while True:
        try:
            return int(input(f"Ingrese el número {indice}: "))
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingrese un número entero.")

# Pedimos y validamos los tres números
num1 = pedir_numero(1)
num2 = pedir_numero(2)
num3 = pedir_numero(3)

# Determinar el mayor
if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

# Mostrar resultado
print(f"✅ El número mayor entre {num1}, {num2} y {num3} es: {mayor}")
