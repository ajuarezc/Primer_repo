class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

# Crear una instancia de la clase
calc = Calculadora()

# Mostrar un menú al usuario
print("=== CALCULADORA BÁSICA ===")
print("1. Sumar")
print("2. Restar")

opcion = input("Elige una opción (1 o 2): ")

# Pedir los números solo si la opción es válida
if opcion == "1" or opcion == "2":
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        resultado = calc.sumar(a, b)
        print("El resultado de la suma es:", resultado)
    elif opcion == "2":
        resultado = calc.restar(a, b)
        print("El resultado de la resta es:", resultado)
else:
    print("Opción no válida. Por favor, elige 1 o 2.")
