from funciones import tipo_usuario

def menu_usuario(nombre):
    opcion=""
    while opcion != "4":
        print("\n---MENU DE USUARIO---")
        print("1.- Ver informacion")
        print("2.- Consultar datos")
        print("3.- Reaizar una operacion")
        print("4.. Cerrar sesión")
        opcion=input("Elija una opcion: ")

        match opcion:
            case "1":
                print("Nombre de usuario",nombre)
                print("tipo de usuario",tipo_usuario(nombre))
            case "2":
                print("Consulta de datos")
            case "3":
                print("Realizar una operacion")
            case "4":
                print("Cerrando sesion")
            case _:
                print("Opcion invalida")    



