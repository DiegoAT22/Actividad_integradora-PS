#conversor 
# conversor.py

TASA_DOLAR = 18.50


def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def kilometros_a_millas(kilometros):
    return kilometros * 0.621371


def millas_a_kilometros(millas):
    return millas / 0.621371


def pesos_a_dolares(pesos):
    return pesos / TASA_DOLAR


def dolares_a_pesos(dolares):
    return dolares * TASA_DOLAR


def menu():
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Kilómetros a Millas")
    print("4. Millas a Kilómetros")
    print("5. Pesos Mexicanos a Dólares")
    print("6. Dólares a Pesos Mexicanos")

    opcion = input("Selecciona una opción: ")

    try:
        valor = float(input("Ingresa el valor a convertir: "))

        if opcion == "1":
            resultado = celsius_a_fahrenheit(valor)
        elif opcion == "2":
            resultado = fahrenheit_a_celsius(valor)
        elif opcion == "3":
            resultado = kilometros_a_millas(valor)
        elif opcion == "4":
            resultado = millas_a_kilometros(valor)
        elif opcion == "5":
            resultado = pesos_a_dolares(valor)
        elif opcion == "6":
            resultado = dolares_a_pesos(valor)
        else:
            print("Opción inválida.")
            return

        print(f"Resultado: {resultado:.2f}")

    except ValueError:
        print("Error: debes ingresar un valor numérico.")


if __name__ == "__main__":
    menu()