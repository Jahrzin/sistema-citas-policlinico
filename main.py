# Guarda los datos en el archivo en la variable
nombre_del_archivo = "citas_policlinico.txt"

def cargar_citas():
    # Guardar todas las citas en la variable
    lista_de_citas = []

    try:
        archivo = open(nombre_del_archivo, "r", encoding="utf-8") #Archivo se va leer y con simbolos en español

        for fila in archivo:  # Bucle para busqueda de cada fila por fila
            fila_limpia = fila.strip() # Limpia el texto de los espacios y espacios en blancos

            if fila_limpia != "":  # Verifica si tiene texto en el ""
                datos_separados = fila_limpia.split(",") # Separa los texto en ,

                # Datos ingresados para la cita
                if len(datos_separados) == 4:
                    ficha_del_paciente = {
                        "codigo": datos_separados[0],
                        "dni": datos_separados[1],
                        "nombre": datos_separados[2],
                        "especialidad": datos_separados[3],
                    }

                    # Los datos ingresado se guarda en la varible ya como cita
                    lista_de_citas.append(ficha_del_paciente)

        # Termina el archivo despues de crear la cita
        archivo.close()

     # Si el archivo .txt todavía no existe en la lista, ignora el error y continúa el menu si que aparezca error
    except FileNotFoundError:
     pass # si no se escuentra la lista que se busca, solo regresa al menu principal sin que te salga error
    return lista_de_citas  # Devuelve la lista con las citas, si es que no había archivo, lo que devuelve la lista vacía


def guardar_archivo(cita):
    # El archivo se abre en modo "a" para agregar datos sin borrar los anteriores
    archivo = open(nombre_del_archivo, "a", encoding="utf-8")

    # Se ingresa los datos en las filas de texto que se va a guardar en el .txt
    texto = (
        cita["codigo"]
        + ","
        + cita["dni"]
        + ","
        + cita["nombre"]
        + ","
        + cita["especialidad"]
        + "\n"
    )

    # Guarda y escribe el texto dentro del archivo de .txt
    archivo.write(texto)
    # El archivo se cierra para guardar los cambios
    archivo.close()


def registrar(citas):
    print("\n--- REGISTRAR NUEVA CITA ---")

    # Bucle para repetir el pedido hasta que el usuario ingrese un DNI válido
    while True:
        dni = input("Ingrese DNI (8 digitos): ")
        if len(dni) == 8 and dni.isdigit(): # Verifica que el DNI tenga exactamente 8 caracteres y sean solo números
            break # El bucle termina porque el DNI es correcto
        else:
            print("Error: El DNI debe ser de 8 números.")

    # Se utiliza bucle para que se ingrese al menos nombre y apellido (mínimo 2 palabras)
    while True:
        nombre = input("Ingrese nombres y apellidos: ").strip()

        # 1. Verifica que tenga al menos 2 palabras nombre + apellido
        if (
            len(nombre.split()) >= 2 # len(nombre.split()) >= 2 exige mínimo 2 palabras (nombre + apellido), cortando las palabras con los espacios en blanco
            and nombre.replace(" ", "").isalpha() # nombre.replace(" ", "").isalpha() asegura que solo haya letras sin números ni símbolos
        ):
            break
        else:
            print(
                "Error: Debe ingresar al menos un nombre y un apellido (solo letras, sin números)."
            )

    especialidades_validas = [
        "MEDICINA GENERAL",
        "PEDIATRÍA",
        "PEDIATRIA",
        "ODONTOLOGÍA",
        "ODONTOLOGIA",
        "OBSTETRICIA",
    ]

    while True:
        especialidad = input(
            "Ingrese especialidad (Medicina General, Pediatría, Odontología, Obstetricia): " ).strip()

        # Verifica si lo que escribió el usuario está dentro de la lista permitida
        if especialidad.upper() in especialidades_validas:
            break  # Opción correcta, sale del bucle
        else:
            print(
                "Error: Especialidad no válida. Debe elegir entre: Medicina General, Pediatría, Odontología u Obstetricia.")

    num = len(citas) + 1     # Se obtiene el total de cuantas citas se crearon
    codigo = "CIT-" + str(num).zfill(3) # Genera codigo único del paciente combinando "CIT-" y su número de turno

    # Con los datos ingresado se crea la ficha de la nueva cita
    nueva = {
        "codigo": codigo,
        "dni": dni,
        "nombre": nombre,
        "especialidad": especialidad,
    }

    citas.append(nueva) # Se agrega la cita a la lista de citas creadas
    guardar_archivo(nueva) # Guarda la cita en el archivo .txt para que no se borre
    print("¡Cita registrada con éxito! Su codigo es:", codigo) 


def mostrar(citas):
    print("\n--- LISTA DE CITAS ---")
    if len(citas) == 0: # Verifica si la lista no tiene ninguna cita guardada 
        print("No hay citas registradas todavia.")
        return # Si no hay citas, no pasaria al for para el bucle 
    for cita in citas: # Muestra los datos de la cita buscada por el bucle, mostrando el resultado
        print(
            "Codigo:",
            cita["codigo"],
            "| DNI:",
            cita["dni"],
            "| Paciente:",
            cita["nombre"],
            "| Especialidad:",
            cita["especialidad"],
        )


def buscar(citas):
    print("\n--- BUSCAR CITA ---")
    if len(citas) == 0: # Verifica si la lista está vacía antes de hacer la búsqueda
        print("No hay registros para buscar.")
        return # Sale de la función porque no hay nada que buscar Si no hay citas guardadas en la lista, se termina la busqueda de cita

    #  Se pide el código y con .upper() hace que se convierta las letras a mayúsculas para evitar errores en la busqueda
    codigo_buscado = input(
        "Ingrese el codigo de la cita (ej: CIT-001): "
    ).upper()
    encontrado = False # Se utiliza la variable false para saber si encontramos o no la cita
   
    for cita in citas: # Bucle para para la busqueda de cada cita de la lista
        if cita["codigo"] == codigo_buscado: # El bucle buscara el codigo que sea igual a la variable codigo_buscado, mostrando la cita que se busca
            print("\n¡Encontrado!")
            print("Codigo:", cita["codigo"])
            print("DNI:", cita["dni"])
            print("Paciente:", cita["nombre"])
            print("Especialidad:", cita["especialidad"])
            encontrado = True # La variable encontrada pasa a verdadero, de que sí existe la cita
            break # Se detiene el bucle, al terminar la bsuqueda

    if not encontrado: # Si no se encuentra la cita, la variable sigue en False,  lo que avisa que la cita no existe
        print("No se encontro ninguna cita con ese codigo.")


def ordenar(citas):
    print("\n--- ORDENAR CITAS ---")
    if len(citas) == 0: # Se revisa si la lista está vacía antes de que comienze a ordenar
        print("No hay citas para ordenar.")
        return # Termina si no se encuentra cita en la lista, haciendo que no comienze a ordenar

    # Ordena la lista de citas de forma ascendente según la clave "codigo"
    citas.sort(key=lambda x: x["codigo"])
    print("¡Citas ordenadas por codigo correctamente!")
    mostrar(citas) # Se mostrar la lista ya organizada de forma ascendente

def reiniciar_citas(citas):
    confirmacion = (
        input(
            "¿Está seguro de que desea borra todas las citas? (S/N): "
        ).strip() .upper() )

    if confirmacion == "S":
        # Al abrir con "w", Python borra todo el contenido del archivo .txt
        archivo = open(nombre_del_archivo, "w", encoding="utf-8")
        archivo.close()

        citas.clear()  # Vaciamos la lista en memoria
        print("¡Todas las citas han sido eliminadas correctamente!")
    else:
        print("Operación cancelada.")

def main(): # Inicio el codigo para la busqueda, registrar, ordenar y salida del codigo

    # Las citas guardadas se cargar previamente en el archivo .txt al iniciar el programa    
    citas = cargar_citas()

    while True: # Se utiliza un bucle infinito para mantener el menú activo hasta que el usuario decida salir del menu, haciendo que el bucle termine
        print("\n=== SISTEMA DE CITAS - POLICLINICO ===")
        print("1. Registrar cita")
        print("2. Ver todas las citas")
        print("3. Buscar por codigo")
        print("4. Ordenar citas")
        print("5. Eliminar cita")
        print("6. Salir")

        opcion = input("Elige una opcion (1-5): ") # La consola lee la opción que es ingresada por el usuario

        # La consola evalúa la opción seleccionada y ejecuta la función que eligío el usuario
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
        elif opcion == "5":
            print("Saliendo del programa...")
            break # Se detiene el bucle while, haciendo que finalize el programa
        else:
            print("Opcion no valida, elige del 1 al 5.")

# Asegura que el programa empiece a ejecutar desde la función principal main()
if __name__ == "__main__":
    main()