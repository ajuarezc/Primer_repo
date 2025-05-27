class Suma:
    def sumar(self, a, b):
        return a + b

sumar_obj = Suma()

a = int(input("INGRESA EL PRIMER NÚMERO: "))
b = int(input("INGRESA EL SEGUNDO NÚMERO: "))

resultado = sumar_obj.sumar(a, b)

print("LA SUMA ES:", resultado)
