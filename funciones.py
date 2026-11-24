nombre_del_archivo = "citas_policlinico.txt"

def cargar_citas():
    lista_de_citas = []
    try:
        archivo = open(nombre_del_archivo, "r", encoding="utf-8")
        for fila in archivo:
            fila_limpia = fila.strip()
            if fila_limpia != "":
                datos_separados = fila_limpia.split(",")
                if len(datos_separados) == 4:
                    codigo, dni, nombre, especialidad = datos_separados

                    ficha_del_paciente = {
                        "codigo": codigo,
                        "dni": dni,
                        "nombre": nombre,
                        "especialidad": especialidad,
                    }
                    lista_de_citas.append(ficha_del_paciente)
        archivo.close()
    except FileNotFoundError:
        pass
    return lista_de_citas

def guardar_archivo(cita):
    archivo = open(nombre_del_archivo, "a", encoding="utf-8")
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
    archivo.write(texto)
    archivo.close()


def registrar(citas):
    print("\n--- REGISTRAR NUEVA CITA ---")
    while True:
        dni = input("\nIngrese su DNI (8 dígitos): ")
        if len(dni) == 8 and dni.isdigit():
            break
        else:
            print("\nError en el DNI, debe tener 8 dígitos.")

    # Pide los nombres (acepta letras y numeros)
    while True:
        nombres = input("\nIngresar su nombre: ").strip()
        if len(nombres) > 0 and nombres.replace(" ", "").isalnum():
            break
        else:
            print("\nError: El nombre solo puede contener letras y numeros.")

    # Pide los apellidos (acepta solo letras)
    while True:
        apellidos = input("\nIngresar su apellido: ").strip()
        if len(apellidos) > 0 and apellidos.replace(" ", "").isalpha():
            break
        else:
            print("\nError: El apellido solo debe contener letras, sin numeros.")

    # Une ambos en una sola variable para guardarlos juntos
    nombre = nombres + " " + apellidos

    especialidades_validas = [
        "MEDICINA GENERAL",
        "PEDIATRIA",
        "ODONTOLOGIA",
        "OBSTETRICIA",
    ]

    while True:
        especialidad = input(
            "\nIngrese especialidad (Medicina General, Pediatria, Odontologia, Obstetricia): "
        ).strip()
        if especialidad.upper() in especialidades_validas:
            break
        else:
            print(
                "\nHubo un error en la selección de la especialidad. Debe elegir entre: Medicina General, Pediatria, Odontologia u Obstetricia."
            )

    num = len(citas) + 1
    codigo = "CIT-" + str(num).zfill(3)

    nueva = {
        "codigo": codigo,
        "dni": dni,
        "nombre": nombre,
        "especialidad": especialidad,
    }

    citas.append(nueva)
    guardar_archivo(nueva)
    print("\n¡Cita registrada con éxito! Su codigo es:", codigo)

def mostrar(citas):
    print("\n--- LISTA DE CITAS ---")
    if len(citas) == 0:
        print("\nNo hay citas registradas todavia.")
        return
    for cita in citas:
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
    if len(citas) == 0:
        print("\nNo hay registros para buscar.")
        return

    codigo_buscado = input("\nIngrese el codigo de la cita (ej: CIT-001): ").strip().upper()
    encontrado = False

    for cita in citas:
        if cita["codigo"] == codigo_buscado:
            print("\n¡Encontrado!")
            print("Codigo:", cita["codigo"])
            print("DNI:", cita["dni"])
            print("Paciente:", cita["nombre"])
            print("Especialidad:", cita["especialidad"])
            encontrado = True
            break

    if not encontrado:
        print("\n No se encontro ninguna cita con ese codigo.")

def ordenar(citas):
    print("\n--- ORDENAR Y FILTRAR CITAS ---")
    if len(citas) == 0: # Revisa si la lista esta vacia antes de hacer nada
        print("\nNo hay citas registradas para ordenar.")
        return

    print("\nComo deseas organizar las citas?")
    print("1. Ordenar alfabeticamente por nombre del paciente")
    print("2. Ver solo las citas de una especialidad")
    print("3. Ver desde la ultima cita registrada hasta la primera")

    opcion = input("\n Elige una opcion (1-3): ").strip()

    if opcion == "1":
        # Ordena la lista completa usando el nombre del paciente (de menor a mayor)
        citas.sort(key=lambda x: x["nombre"].lower())
        print("\n¡Listo! Citas ordenadas por nombre del paciente:")
        mostrar(citas)

    elif opcion == "2":
        print("\n--- SELECCIONA UNA ESPECIALIDAD ---")
        print("1. Medicina General")
        print("2. Pediatria")
        print("3. Odontologia")
        print("4. Obstetricia")

        op_esp = input("\nElige el numero de la especialidad (1-4): ").strip()

        # Relaciona el numero elegido con el nombre de la especialidad
        lista_especialidades = {
            "1": "MEDICINA GENERAL",
            "2": "PEDIATRIA",
            "3": "ODONTOLOGIA",
            "4": "OBSTETRICIA",
        }

        if op_esp in lista_especialidades:
            especialidad_elegida = lista_especialidades[op_esp]
            print(f"\n--- PACIENTES DE {especialidad_elegida} ---")
            se_encontro = False

            # Busca y muestra unicamente las citas que coinciden con esa especialidad
            for cita in citas:
                if cita["especialidad"].upper() == especialidad_elegida:
                    print(
                        "Codigo:",
                        cita["codigo"],
                        "| DNI:",
                        cita["dni"],
                        "| Paciente:",
                        cita["nombre"],
                    )
                    se_encontro = True

            if not se_encontro:
                print(f"\nAun no hay pacientes registrados en {especialidad_elegida}.")
        else:
            print("\nError: Debes elegir un numero del 1 al 4.")

    elif opcion == "3":
        # Invierte el orden de los codigos para mostrar primero los mas nuevos
        citas.sort(key=lambda x: x["codigo"], reverse=True)
        print("\n¡Listo! Mostrando desde la cita mas reciente hasta la mas antigua:")
        mostrar(citas)

    else:
        print("\nError: Opcion no valida. Regresando al menu principal...")

def reiniciar_citas(citas):
    confirmacion = (
        input("\n¿Está seguro de que desea borra todas las citas? (S/N): ")
        .strip()
        .upper()
    )

    if confirmacion == "S":
        archivo = open(nombre_del_archivo, "w", encoding="utf-8")
        archivo.close()
        citas.clear()
        print("\n¡Todas las citas han sido eliminadas correctamente!")
    else:
        print("\nOperación cancelada.")