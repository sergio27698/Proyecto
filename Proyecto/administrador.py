from funciones import registrar_usuario,mostrar_usuario,buscar_usuario,modificar_usuario,eliminar_usuario
def menu_administrador():
    opcion=""
    while opcion != "6":
        print("\n---MENU DEL ADMINISTRADOR---")
        print("1.- Registrar usuario")
        print("2.- Mostrar usuario")
        print("3.- Buscar usuario")
        print("4.- Modificar usuario")
        print("5.- Eliminar usario")
        print("6.- Cerrar sesion")
        opcion=input("Elija una opcion: ")

        match opcion:
            case "1":
                registrar_usuario()
            case "2":
                mostrar_usuario()
            case "3":
                buscar_usuario()
            case "4":
                modificar_usuario()
            case "5":
                eliminar_usuario()
            case "6":
                print("Cerrando sesión")
            case _:
                print("Opcion incorrecta")
    

                            