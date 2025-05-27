class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

# Crear una instancia de la clase
calc = Calculadora()

# Mostrar un menú al usuario
print("=== CALCULADORA BÁSICA ===")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")

opcion = input("Elige una opción (1, 2 o 3): ")

# Pedir los números solo si la opción es válida
if opcion in ("1", "2", "3"):
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        resultado = calc.sumar(a, b)
        print("El resultado de la suma es:", resultado)
    elif opcion == "2":
        resultado = calc.restar(a, b)
        print("El resultado de la resta es:", resultado)
    elif opcion == "3":
        resultado = calc.multiplicar(a, b)
        print("El resultado de la multiplicación es:", resultado)
else:
    print("Opción no válida. Por favor, elige 1, 2 o 3.")
