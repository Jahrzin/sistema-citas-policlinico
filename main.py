from funciones import (
    cargar_citas,
    registrar,
    mostrar,
    buscar,
    ordenar,
    reiniciar_citas,
)

def main():
    citas = cargar_citas()

    while True:
        print("\n=== SISTEMA DE CITAS - POLICLINICO ===")
        print("1. Registrar cita")
        print("2. Ver todas las citas")
        print("3. Buscar por codigo")
        print("4. Ordenar citas")
        print("5. Eliminar cita")
        print("6. Salir")

        opcion = input("\nElige una opcion (1-6): ")

        if opcion == "1":
            registrar(citas)
        elif opcion == "2":
            mostrar(citas)
        elif opcion == "3":
            buscar(citas)
        elif opcion == "4":
            ordenar(citas)
        elif opcion == "5":
            reiniciar_citas(citas)
        elif opcion == "6":
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpcion no valida, elige del 1 al 6.")

if __name__ == "__main__":
    main()