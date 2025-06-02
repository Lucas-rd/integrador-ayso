print("=== Calculadora de dos números ===")

# Ingreso de datos por el usuario
num1 = float(input("Ingresá el primer número: "))
num2 = float(input("Ingresá el segundo número: "))

# Lista para almacenar resultados
resultados = []

# Cálculos y guardado en la lista
resultados.append(("Suma", num1 + num2))
resultados.append(("Resta", num1 - num2))
resultados.append(("Multiplicación", num1 * num2))

# División con verificación de división por cero
if num2 != 0:
    resultados.append(("División", num1 / num2))
else:
    resultados.append(("División", "No se puede dividir por cero"))

# Mostrar resultados con ciclo for
print("\n=== Resultados ===")
for operacion, resultado in resultados:
    print(f"{operacion}: {resultado}")
