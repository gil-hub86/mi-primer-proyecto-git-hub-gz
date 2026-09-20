# 1. Entrada de datos (convertidos a enteros)
año_actual = 2026

año_hijo1 = int(input("¿En qué año nació tu primer hijo? "))
año_hijo2 = int(input("¿En qué año nació tu segundo hijo? "))


# 2. Operación matemática (cálculo de edades y suma)
edad_hijo1 = año_actual - año_hijo1
edad_hijo2 = año_actual - año_hijo2
suma_edades = edad_hijo1 + edad_hijo2


# 3. salida de datos
print(f"\nEste año tu primer hijo cumplirá: {edad_hijo1} años.")
print(f"Este año tu segundo hijo cumplirá: {edad_hijo2} años.")
print(f"La suma de las dos edades es: {suma_edades} años.")

# 4.Estructura condicional (¿Quien es mayor?)
if edad_hijo1 > edad_hijo2:
    print("Tu primer hijo es el mayor.")

elif edad_hijo2 > edad_hijo1:
    print("Tu segundo hijo es el mayor.")

else:
    print("¡Tus dos hijos tienen la misma edad!")
