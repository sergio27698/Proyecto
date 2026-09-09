usuarios= {"Sergio":{"contraseña":"00000","tipo":"administrador"}}
def ver_credenciales(nombre,contraseña):
    if nombre in usuarios and usuarios[nombre]["contraseña"]== contraseña:
        return True
    return False

def tipo_usuario(nombre):
    try:
        return usuarios[nombre]["tipo"]
    except KeyError:
        return None

def registrar_usuario():
    nombre=input("Ingrese el nombre de usuario: ")
    if nombre in usuarios:
       print("Ese usuario ya existe")
       return

    contraseña=input("Ingrese su contraseña: ")
    usuarios[nombre]={"contraseña":contraseña,"tipo":"usuario"}
    print("Usuario registrado")

def mostrar_usuario():
    print("Lista de usuarios registrados")
    for nombre in usuarios:
        print("-",nombre,"("+ usuarios[nombre]["tipo"]+")")

def buscar_usuario():
    nombre=input("Ingrese el nombre del usuario a buscar: ")
    if nombre in usuarios:
        print("Usuario encontrado:")
        print("Nombre",nombre)
        print("Tipo:",usuarios[nombre]["tipo"])
    else:
        print("El usuario no exsite")

def modificar_usuario():
    nombre=input("Ingrese el usuario a modificar: ")
    if nombre not in usuarios:
        print("El usuario no existe")
        return

    nueva_contraseña=input("Ingrese la nueva contraseña: ")
    usuarios[nombre]["contraseña"]=nueva_contraseña
    print("Contraseña actualizada")

def eliminar_usuario():
    nombre=input("Ingrese el usuario a eliminar: ")
    if nombre in usuarios:
        del usuarios[nombre]
        print("Usuario eliminado")
    else:
        print("El usario no existe")           