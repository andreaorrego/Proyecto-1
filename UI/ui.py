from API import api

def pedir_departamento():
    return input("\nIngrese el departamento: ")

def pedir_limite_registros():
    while True:
        try:
            limite = int(input("\nIngrese el numero de registros (1-1000): "))
            if 1 <= limite <= 1000:
                return limite
            print("El numero debe estar entre 1 y 1000.")
        except ValueError:
            print("Ingrese un numero entero valido.")

def mostrar_menu():
    print("\nConsultar datos")
    print("\n1. Consultar casos")
    print("2. Salir")
    return input("\nSeleccione una opcion: ")

def resultado(nombre_municipio, nombre_departamento, edad, tipo_contagio, estado, pais_procedencia):
    return (
        "Ciudad de ubicacion: {}\n"
        "Departamento: {}\n"
        "Edad: {}\n"
        "Tipo de contagio: {}\n"
        "Estado: {}\n"
        "Pais de procedencia: {}"
    ).format(
        nombre_municipio,
        nombre_departamento,
        edad,
        tipo_contagio,
        estado,
        pais_procedencia if pais_procedencia is not None else "N/A"
    )

def mostrar_resultados(df):
    if df.empty:
        print("\nNo se encontraron registros para mostrar.")
        return

    print("\n" + "=" * 40)
    for _, fila in df.iterrows():
        texto = resultado(
            fila["nombre_municipio"],
            fila["nombre_departamento"],
            fila["edad"],
            fila["tipo_contagio"],
            fila["estado"],
            fila["pais_procedencia"]
        )
        print(texto)
        print("-" * 40)

        