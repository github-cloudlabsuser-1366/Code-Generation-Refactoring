import math

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b
100
def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero no permitida"
    return a / b

def factorial(n):
    if n < 0:
        return "Error: No se puede calcular el factorial de un número negativo"
    if n > 170:  # Límite razonable para evitar desbordamiento
        return "Error: El número es demasiado grande para calcular su factorial"
    try:
        return math.factorial(n)
    except OverflowError:
        return "Te pasaste pibe!!"

def menu():
    print("Calculadora Básica")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Factorial")
    print("6. Salir")

while True:
    menu()
    opcion = input("Selecciona una opción (1-6): ")

    if opcion == "6":
        print("Saliendo de la calculadora...")
        break

    if opcion in ["1", "2", "3", "4"]:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            print(f"Resultado: {sumar(num1, num2)}")
        elif opcion == "2":
            print(f"Resultado: {restar(num1, num2)}")
        elif opcion == "3":
            print(f"Resultado: {multiplicar(num1, num2)}")
        elif opcion == "4":
            print(f"Resultado: {dividir(num1, num2)}")

    elif opcion == "5":
        num = int(input("Ingresa un número para calcular su factorial: "))
        print(f"Resultado: {factorial(num)}")

    else:
        print("Opción no válida. Intenta de nuevo.")
