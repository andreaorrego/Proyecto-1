from API import api
from UI import ui

def main():
    while True:
        opcion = ui.mostrar_menu()
        
        if opcion == "1":
            depto = ui.pedir_departamento()
            limite = ui.pedir_limite_registros()
            
            print(f"\nConsultando {limite} registros de {depto}...")
            datos = api.cargar_datos(limite, depto)
            
            ui.mostrar_resultados(datos)

        elif opcion == "2":
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpcion no valida, intente nuevamente.")

if __name__ == "__main__":
    main()